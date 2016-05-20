from django.contrib import admin

from .models import Client, Project


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('department', 'agency',)
    list_filter = ('department',)
    search_fields = ('department', 'agency',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'client',)
    list_filter = ('status', 'billable', 'cloud_dot_gov',)
    search_fields = ('name',)
