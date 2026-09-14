from django.contrib import admin
from .models import AppointmentRequest


@admin.register(AppointmentRequest)
class AppointmentRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "branch", "service", "preferred_date", "created_at")
    list_filter = ("branch", "service")
    search_fields = ("name", "phone", "email")
