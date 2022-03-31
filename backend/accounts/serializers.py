from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'nickname', 'email']
        extra_kwargs = {'password' : {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            nickname=validated_data['nickname'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserBodySerializer(serializers.Serializer):
    username = serializers.CharField(help_text="아이디")
    password = serializers.CharField(help_text="비밀번호")
    nickname = serializers.CharField(help_text="닉네임")
    email = serializers.CharField(help_text="이메일")