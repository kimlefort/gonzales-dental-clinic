from django.shortcuts import render
from django.http import Http404
from django.views.decorators.http import require_GET
from .content import BRANCHES, SERVICES, FAQS, HISTORY


def context(request, **extra):
    selected = next((b for b in BRANCHES if b['id'] == request.GET.get('branch')), BRANCHES[0])
    return dict(branches=BRANCHES, services=SERVICES, selected_branch=selected,
                faqs=FAQS, history=HISTORY, **extra)


@require_GET
def home(request):
    return render(request, 'clinic/campaign.html', context(request, page='home'))


@require_GET
def information(request, page):
    titles = {'about': 'About Gonzales Dental', 'history': 'Our history',
              'services': 'Explore our services', 'faqs': 'Before your visit', 'clinics': 'Our clinics'}
    if page not in titles:
        raise Http404
    return render(request, 'clinic/information.html', context(request, page=page, page_title=titles[page]))


@require_GET
def service_detail(request, slug):
    service = next((s for s in SERVICES if s['slug'] == slug), None)
    if not service:
        raise Http404
    return render(request, 'clinic/service_detail.html', context(request, page='services', service=service, page_title=service['name']))


@require_GET
def branch_detail(request, slug):
    branch = next((b for b in BRANCHES if b['id'] == slug), None)
    if not branch:
        raise Http404
    data = context(request, page='branch', page_title=branch['name'] + ' clinic')
    data['selected_branch'] = branch
    return render(request, 'clinic/branch.html', data)
