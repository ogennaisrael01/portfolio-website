from django.core.management.base import BaseCommand
from portfolio.models import Skill, Experience, Education, Project
from datetime import date


class Command(BaseCommand):
    help = "Seed the database with initial skills, education, and experience data"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Seeding database..."))

        # # === Skills ===
        skills_data = [
            {"name": "Python", "level": 95, "category": "backend", "icon": "fab fa-python"},
            {"name": "Django", "level": 90, "category": "backend", "icon": "fas fa-leaf"},
            {"name": "Django REST Framework", "level": 85, "category": "backend", "icon": "fas fa-plug"},
            {"name": "PostgreSQL", "level": 80, "category": "database", "icon": "fas fa-database"},
            {"name": "Git & GitHub", "level": 85, "category": "tools", "icon": "fab fa-git-alt"},
            {"name": "Docker", "level": 70, "category": "tools", "icon": "fab fa-docker"},
        ]
        for skill in skills_data:
            Skill.objects.get_or_create(**skill)

        # === Education ===
        edu_data = [
            {
                "institution": "University of Backend Tech",
                "degree": "Bachelor of Science",
                "field_of_study": "Computer Science",
                "start_date": date(2018, 9, 1),
                "end_date": date(2022, 6, 30),
                "current": False,
            },
            {
                "institution": "Self Learning / Online Courses",
                "degree": "Certification",
                "field_of_study": "Backend Development (Python & Django)",
                "start_date": date(2022, 7, 1),
                "end_date": None,
                "current": True,
            },
        ]
        for edu in edu_data:
            Education.objects.get_or_create(**edu)

        # === Experience ===
        exp_data = [
            {
                "company": "Tech Solutions Ltd",
                "position": "Backend Developer (Intern)",
                "description": "Developed REST APIs, worked with PostgreSQL, and optimized backend logic for scalability.",
                "start_date": date(2022, 9, 1),
                "end_date": date(2023, 2, 28),
                "current": False,
            },
            {
                "company": "Freelance",
                "position": "Backend Developer",
                "description": "Built Django-based applications, managed deployments, and implemented authentication & permissions.",
                "start_date": date(2023, 3, 1),
                "end_date": None,
                "current": True,
            },
        ]
        for exp in exp_data:
            Experience.objects.get_or_create(**exp)
