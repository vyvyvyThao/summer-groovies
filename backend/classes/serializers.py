from rest_framework import serializers 
from .models import Class

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = [
            'title',
            'start_date',
            'end_date',
            'schedule',
            'description',
            'slots_remaining'
        ]