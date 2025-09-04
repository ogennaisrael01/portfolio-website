from django.core.management.base import BaseCommand
from portfolio.models import Project
from django.core.files import File
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Seeds the database with sample projects'

    def handle(self, *args, **kwargs):
        projects_data = [
            {
                "title": "Blog API",
                "description": "A REST API for managing blog posts, comments, and users with JWT authentication.",
                "short_description": "REST API for blog management",
                "image_path": "projects/blog_api.png",
                "tech_stack": "Python, Django, Django REST Framework, JWT, PostgreSQL",
                "github_url": "https://github.com/yourusername/blog-api",
                "live_url": "",
                "featured": True
            },
            {
                "title": "E-Commerce Platform",
                "description": "Full-stack e-commerce platform with cart, orders, and payment integration.",
                "short_description": "E-Commerce platform with payment",
                "image_path": "projects/ecommerce.png",
                "tech_stack": "Python, Django, Stripe API, PostgreSQL, HTML, CSS, JavaScript",
                "github_url": "https://github.com/yourusername/ecommerce",
                "live_url": "",
                "featured": True
            },
            {
                "title": "Chat App",
                "description": "Real-time chat application using Django Channels and WebSockets.",
                "short_description": "Real-time chat app",
                "image_path": "projects/chat_app.png",
                "tech_stack": "Python, Django, Django Channels, WebSockets, Redis",
                "github_url": "https://github.com/yourusername/chat-app",
                "live_url": "",
                "featured": True
            }
        ]

        for proj in projects_data:
            project = Project(
                title=proj["title"],
                description=proj["description"],
                short_description=proj["short_description"],
                tech_stack=proj["tech_stack"],
                github_url=proj["github_url"],
                live_url=proj["live_url"],
                featured=proj["featured"]
            )

            image_full_path = os.path.join(settings.MEDIA_ROOT, proj["image_path"])
            if os.path.exists(image_full_path):
                with open(image_full_path, "rb") as f:
                    project.image.save(os.path.basename(proj["image_path"]), File(f), save=True)
                self.stdout.write(self.style.SUCCESS(f"Created project: {project.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"Image not found: {image_full_path}"))
