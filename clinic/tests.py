from django.test import TestCase
from .content import BRANCHES, SERVICES, FAQS
from django.urls import reverse
from html.parser import HTMLParser
from .models import AppointmentRequest


class WebsiteTests(TestCase):
    def test_home_includes_published_tagline_and_service_options(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Three Generations of Dental Care')
        self.assertContains(response, 'class="service-card"', count=10)
        for option in ('Invisalign', 'Emax veneers', 'Operculectomy', 'Root canal treatment'):
            self.assertContains(response, option)
        self.assertNotContains(response, 'Mintal')

    def test_branch_links_work_without_javascript(self):
        for branch in BRANCHES:
            response = self.client.get('/', {'branch': branch['id']})
            self.assertEqual(response.context['selected_branch']['id'], branch['id'])
            self.assertContains(response, 'id="contact-call" href="tel:' + branch['tel'] + '"')
            self.assertContains(response, 'id="contact-facebook" href="' + branch['facebook'] + '"')

    def test_invalid_branch_falls_back_without_injecting_input(self):
        response = self.client.get('/', {'branch': '<script>alert(1)</script>'})
        self.assertEqual(response.context['selected_branch']['id'], 'obrero')
        self.assertNotContains(response, '<script>alert(1)</script>')

    def test_no_fake_booking_endpoint(self):
        response = self.client.post('/', {'name': 'Test'})
        self.assertEqual(response.status_code, 405)
        self.assertEqual(AppointmentRequest.objects.count(), 0)

    def test_information_pages_are_internal_and_render(self):
        for name in ('about', 'history', 'services', 'faqs', 'clinics'):
            with self.subTest(page=name):
                response = self.client.get(reverse(name), {'branch': 'digos'})
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.context['selected_branch']['id'], 'digos')
                self.assertContains(response, 'noindex,nofollow')
                self.assertNotContains(response, 'href="https://gonzalesdentalclinic.wordpress.com')

    def test_every_service_has_a_working_detail_page(self):
        for service in SERVICES:
            with self.subTest(service=service['slug']):
                response = self.client.get(reverse('service', args=[service['slug']]))
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, service['description'])
                self.assertContains(response, 'Published treatment options')

    def test_branch_route_takes_precedence_over_conflicting_query(self):
        for branch in BRANCHES:
            response = self.client.get(branch['url'], {'branch': 'matina'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.context['selected_branch']['id'], branch['id'])
            self.assertContains(response, 'cid=' + branch['cid'])
            if branch['id'] != 'obrero':
                self.assertNotContains(response, 'obrero-lobby.webp')

    def test_unknown_detail_routes_return_404(self):
        for url in ('/clinics/unknown/', '/services/unknown/'):
            self.assertEqual(self.client.get(url).status_code, 404)

    def test_new_photography_and_horizontal_logo(self):
        response = self.client.get('/')
        for value in ('campaign-portrait.jpg', 'obrero-lobby.webp', 'brand-symbol', 'brand-name'):
            self.assertContains(response, value)
        self.assertNotContains(response, 'campaign-original.png')

    def test_faqs_and_reviews_disclose_limits(self):
        response = self.client.get('/faqs/')
        for faq in FAQS:
            self.assertContains(response, faq['question'])
        self.assertContains(response, 'payment page does not publish')
        response = self.client.get('/')
        self.assertContains(response, 'Preview snapshot, not a live feed')
        self.assertContains(response, 'Checked 14 September 2026')

    def test_rendered_pages_have_unique_ids_and_valid_internal_links(self):
        class Links(HTMLParser):
            def __init__(self):
                super().__init__()
                self.ids, self.links = [], []

            def handle_starttag(self, tag, attrs):
                attrs = dict(attrs)
                if 'id' in attrs:
                    self.ids.append(attrs['id'])
                if tag == 'a' and attrs.get('href', '').startswith('/'):
                    self.links.append(attrs['href'])

        urls = ['/', '/about/', '/about/history/', '/services/', '/faqs/', '/clinics/']
        urls += [b['url'] for b in BRANCHES]
        urls += [reverse('service', args=[s['slug']]) for s in SERVICES]
        checked = set()
        for url in urls:
            parser = Links()
            parser.feed(self.client.get(url).content.decode())
            self.assertEqual(len(parser.ids), len(set(parser.ids)), url)
            for link in parser.links:
                target = link.split('#')[0]
                if target not in checked:
                    self.assertEqual(self.client.get(target).status_code, 200, target)
                    checked.add(target)
