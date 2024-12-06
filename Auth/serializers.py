from rest_framework import serializers
from .models import MyModels

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModels
        fields = ['id', 'name']

    def validate_id(self , value):
        if MyModels.objects.filter(id=value).exists():
             raise serializers.ValidationError("ID already exists.")
        return value