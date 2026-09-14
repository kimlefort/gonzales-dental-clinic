from django.contrib import admin
from django.urls import path
from clinic import views

urlpatterns = [
    path('admin/', admin.site.urls), path('', views.home, name='home'),
    path('about/', views.information, {'page': 'about'}, name='about'),
    path('about/history/', views.information, {'page': 'history'}, name='history'),
    path('services/', views.information, {'page': 'services'}, name='services'),
    path('services/<slug:slug>/', views.service_detail, name='service'),
    path('faqs/', views.information, {'page': 'faqs'}, name='faqs'),
    path('clinics/', views.information, {'page': 'clinics'}, name='clinics'),
    path('clinics/<slug:slug>/', views.branch_detail, name='branch'),
]
