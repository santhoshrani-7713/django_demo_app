from django.db.models import fields
from rest_framework import serializers
from .models import LineA, LineB

class LineASerializer(serializers.ModelSerializer):
    class Meta:
        model = LineA
        fields = '__all__'
    
class LineBSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineB
        fields = '__all__'