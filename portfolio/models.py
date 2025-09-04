from django.db import models
from django.urls import reverse

    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(help_text="Skill level from 1-100")
    category = models.CharField(max_length=50, choices=[
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('tools', 'Tools & Others'),
    ])
    icon = models.CharField(max_length=50, blank=True, help_text="Font Awesome icon class")
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-level', 'name']

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='projects/')
    tech_stack = models.CharField(max_length=500, help_text="Comma-separated technologies")
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    @property
    def get_tech_list(self):
        return [tech.strip() for tech in self.tech_stack.split(',')]
    
    class Meta:
        ordering = ['-created_date']

class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.position} at {self.company}"
    
    class Meta:
        ordering = ['-start_date']

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"{self.degree} from {self.institution}"
    
    class Meta:
        ordering = ['-start_date']


class Certificates(models.Model):
    title = models.CharField(max_length=200)
    issue_date = models.DateField()
    image = models.ImageField(upload_to='certificates/')
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-issue_date']