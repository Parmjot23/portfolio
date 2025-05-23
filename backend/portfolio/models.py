from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    live_url = models.URLField(blank=True)
    repo_url = models.URLField(blank=True)
    featured_image = models.ImageField(upload_to='projects/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tech_stack = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Template(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    zip_file = models.FileField(upload_to='templates/')
    preview_url = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    quote = models.TextField()
    avatar = models.ImageField(upload_to='testimonials/')
    created_at = models.DateTimeField(auto_now_add=True)
