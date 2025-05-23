from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Project, Template, ContactMessage
from .serializers import ProjectSerializer, TemplateSerializer, ContactMessageSerializer

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer

class TemplateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Template.objects.all().order_by('-created_at')
    serializer_class = TemplateSerializer

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all().order_by('-created_at')
    serializer_class = ContactMessageSerializer
    http_method_names = ['post', 'head']
