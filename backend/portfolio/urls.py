from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TemplateViewSet, ContactMessageViewSet

router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('templates', TemplateViewSet)
router.register('contact', ContactMessageViewSet, basename='contact')

urlpatterns = router.urls
