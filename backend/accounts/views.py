from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import GenericAPIView

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema



from .models import User
from .serializers import UserSerializer

# Create your views here.

class AccountManagement(GenericAPIView):

    queryset = User.objects.all()      # Generic Api View는 반드시 포함 해야한다.
    serializer_class = UserSerializer  # 추가한다

    @api_view(['POST'])
    @permission_classes([AllowAny])
    def signup(request):
        serializer = UserSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'error': '회원정보가 저장되지 않았습니다'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
