# portfolio/models.py
from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='team_images/')
    github_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_used = models.CharField(max_length=200, help_text="Comma-separated list of technologies")
    main_image = models.ImageField(upload_to='project_images/')
    live_site_link = models.URLField(blank=True)
    github_repo_link = models.URLField(blank=True)
    # This will link members through the Contribution model
    members = models.ManyToManyField(TeamMember, through='Contribution')

    def __str__(self):
        return self.title

class Contribution(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    member = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    contribution_text = models.CharField(max_length=255, help_text="e.g., 'Developed the API', 'Designed the UI'")

    class Meta:
        unique_together = ('project', 'member') # A member has one type of contribution per project

    def __str__(self):
        return f"{self.member.name} on {self.project.title}"