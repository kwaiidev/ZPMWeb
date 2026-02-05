from django.contrib import admin
from .models import Project, SystemStatus

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "tech_stack", "created_at")
    search_fields = ("title", "tech_stack")
    list_filter = ("created_at",)


@admin.register(SystemStatus)
class SystemStatusAdmin(admin.ModelAdmin):
    list_display = ("swarm_state", "active_nodes", "last_updated")
