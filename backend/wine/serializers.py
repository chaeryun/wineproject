from dataclasses import fields
from rest_framework import serializers
from wine.models import Wine

class WineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wine
        fields = '__all__'


    