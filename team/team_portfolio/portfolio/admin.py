# portfolio/admin.py
from django.contrib import admin
from .models import TeamMember, Project, Contribution

# Use an inline for Contributions, so we can add them directly within a Project
class ContributionInline(admin.TabularInline):
    model = Contribution
    extra = 1 # How many extra forms to show

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tech_used')
    inlines = (ContributionInline,) # Add the inline here

@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ('project', 'member', 'contribution_text')