(() => {
  const branches = JSON.parse(document.getElementById('branch-data').textContent);
  const selects = [...document.querySelectorAll('[data-branch-select]')];
  const cards = [...document.querySelectorAll('[data-branch-card]')];
  cards.forEach(card => {
    const branch = branches.find(b => b.id === card.dataset.branchCard);
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'card-selector';
    button.setAttribute('aria-label', `Select ${branch.name} clinic`);
    button.addEventListener('click', () => selectBranch(branch.id));
    card.append(button);
  });
  const branchMap = document.getElementById('branch-map');
  branchMap.addEventListener('load', () => {
    branchMap.classList.remove('map-changing');
    branchMap.removeAttribute('aria-busy');
  });
  function selectBranch(id, updateUrl = true) {
    const branch = branches.find(b => b.id === id);
    if (!branch) return;
    if (document.body.dataset.page === 'branch' && id !== document.body.dataset.selectedBranch) {
      location.assign(branch.url);
      return;
    }
    selects.forEach(select => { select.value = id; });
    cards.forEach(card => {
      const selected = card.dataset.branchCard === id;
      card.classList.toggle('selected', selected);
      card.querySelector('.card-selector').setAttribute('aria-pressed', String(selected));
    });
    document.getElementById('contact-address').textContent = branch.address;
    document.getElementById('contact-phone').textContent = branch.phone;
    document.getElementById('contact-call').href = `tel:${branch.tel}`;
    document.getElementById('contact-facebook').href = branch.facebook;
    const email = document.getElementById('contact-email');
    email.textContent = branch.email;
    email.href = `mailto:${branch.email}`;
    document.querySelectorAll('[data-branch-name]').forEach(el => { el.textContent = branch.name; });
    document.getElementById('branch-social').href = branch.facebook;
    document.getElementById('map-directions').href = branch.map_url;
    const map = document.getElementById('branch-map');
    if (map.src !== branch.map_embed) {
      map.classList.add('map-changing');
      map.setAttribute('aria-busy', 'true');
      map.src = branch.map_embed;
    }
    map.title = `Google map of Gonzales Dental ${branch.name}`;
    const rating = document.getElementById('review-rating');
    if (rating) {
      rating.textContent = branch.rating;
      document.getElementById('review-count').textContent = branch.review_count;
      document.getElementById('review-plural').textContent = branch.review_count === 1 ? '' : 's';
      document.getElementById('review-link').href = branch.map_url;
    }
    document.querySelectorAll('[data-preserve-branch]').forEach(link => {
      const target = new URL(link.href);
      target.searchParams.set('branch', id);
      link.href = target;
    });
    try { localStorage.setItem('gonzales.branch', id); } catch (_) { /* Storage is optional. */ }
    if (updateUrl) {
      const url = new URL(location.href);
      url.searchParams.set('branch', id);
      history.replaceState(null, '', url);
    }
  }
  const queryBranch = new URL(location.href).searchParams.get('branch');
  let savedBranch;
  try { savedBranch = localStorage.getItem('gonzales.branch'); } catch (_) {}
  const initial = document.body.dataset.page === 'branch' ? document.body.dataset.selectedBranch : (branches.some(b => b.id === queryBranch) ? queryBranch : (branches.some(b => b.id === savedBranch) ? savedBranch : selects[0].value));
  selectBranch(initial, false);
  selects.forEach(select => select.addEventListener('change', () => selectBranch(select.value)));
  document.querySelectorAll('[data-choose-branch]').forEach(link => link.addEventListener('click', event => {
    event.preventDefault();
    selectBranch(link.dataset.chooseBranch);
    location.hash = 'appointment';
    document.getElementById('contact-branch').focus({ preventScroll: true });
  }));
  const filters = [...document.querySelectorAll('[data-filter]')];
  const services = [...document.querySelectorAll('[data-category]')];
  function filterServices(category) {
    filters.forEach(button => {
      const active = button.dataset.filter === category;
      button.classList.toggle('active', active);
      button.setAttribute('aria-pressed', String(active));
    });
    let count = 0;
    services.forEach(card => {
      card.hidden = category !== 'all' && card.dataset.category !== category;
      if (!card.hidden) count++;
    });
    document.getElementById('filter-status').textContent = `${count} services shown`;
  }
  filters.forEach(button => button.addEventListener('click', () => filterServices(button.dataset.filter)));
  document.querySelectorAll('[data-filter-link]').forEach(link => link.addEventListener('click', () => filterServices(link.dataset.filterLink)));
  const toggle = document.querySelector('.menu-toggle');
  const menu = document.getElementById('main-menu');
  function closeMenu() { menu.classList.remove('open'); toggle.setAttribute('aria-expanded', 'false'); toggle.setAttribute('aria-label', 'Open navigation'); }
  toggle.addEventListener('click', () => {
    const open = menu.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
  });
  menu.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
  document.addEventListener('keydown', event => { if (event.key === 'Escape') closeMenu(); });
})();
