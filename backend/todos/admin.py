from django.contrib import admin

from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ["title", "status", "created_at", "updated_at"]
    list_filter = ["status"]
