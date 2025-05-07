from rest_framework import viewsets, permissions
from .models import Project, Indicator
from .serializers import ProjectSerializer, IndicatorSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

class IndicatorViewSet(viewsets.ModelViewSet):
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer
    permission_classes = [permissions.IsAuthenticated]
