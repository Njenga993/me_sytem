from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, IndicatorViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'indicators', IndicatorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
