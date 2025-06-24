from rest_framework import serializers
from .models import Files

class UserSerializer(serializers.ModelSerializer):
         class Meta:
            model= Files
            field= '__all__'