from django.contrib import admin
from .models import Project, Skill, Experience, Education, Certificates

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'created_date']
    list_filter = ['featured', 'created_date']
    search_fields = ['title', 'description']
    list_editable = ['featured']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'level']
    list_filter = ['category']
    search_fields = ['name']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'start_date', 'current']
    list_filter = ['current', 'start_date']
    search_fields = ['company', 'position']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_date', 'current']
    list_filter = ['current', 'start_date']
    search_fields = ['institution', 'degree']

@admin.register(Certificates)
class CertificatesAdmin(admin.ModelAdmin):
    list_display = ['title', 'issue_date']
    search_fields = ['title']