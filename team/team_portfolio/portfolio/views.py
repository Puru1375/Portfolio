# portfolio/views.py
from django.shortcuts import render
from .models import TeamMember, Project

def portfolio_view(request):
    team_members = TeamMember.objects.all()
    # Prefetch related contributions and the member associated with each contribution
    projects = Project.objects.prefetch_related('contribution_set__member').all()
    
    # Static info for the header (can be moved to a model if you want it dynamic)
    team_info = {
        'name': 'Pixel Pioneers',
        'logo_url': '/static/images/image.png', # Example path
        'tagline': 'Crafting Digital Experiences, One Pixel at a Time.'
    }
    
    context = {
        'team_info': team_info,
        'team_members': team_members,
        'projects': projects,
    }
    return render(request, 'portfolio/index.html', context)