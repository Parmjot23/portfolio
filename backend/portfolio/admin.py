from django.contrib import admin
from .models import Category, Project, Template, ContactMessage, Testimonial

admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Template)
admin.site.register(ContactMessage)
admin.site.register(Testimonial)
