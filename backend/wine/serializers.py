from rest_framework import serializers

from wine.models import Wine, Userlikewine

class WineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wine
        fields = '__all__'


class UserlikewineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userlikewine
        fields = '__all__'
