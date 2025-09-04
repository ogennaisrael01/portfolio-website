from django.shortcuts import render
from .models import Project, Skill, Experience, Education, Certificates
def home(request):
    return render(request, 'portfolio/home.html')


def about_view(request):
    skills = Skill.objects.all().order_by("-level")
    education = Education.objects.all().order_by("-id")
    experience = Experience.objects.all().order_by("-id")
    certificates = Certificates.objects.all().order_by("-id")

    context = {
        "skills": skills,
        "education": education,
        "experience": experience,
        "certificates": certificates
    }
    return render(request, "portfolio/about.html", context)


def project_view(request):
    projects = Project.objects.all().order_by("-id")
    context = {
        "projects": projects
    }
    return render(request, "portfolio/projects.html", context)