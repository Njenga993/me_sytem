from rest_framework import serializers
from .models import Project, Indicator

class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicator
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    indicators = IndicatorSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
