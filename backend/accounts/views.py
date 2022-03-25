from django.http import JsonResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import User
from .serializers import UserSerializer

# Create your views here.

class AccountManagement(APIView):

    @api_view(["GET"])
    @permission_classes([AllowAny])
    def get_user_list(request):
        user_list = User.objects.all()
        user_list_serializer = UserSerializer(user_list, many=True)
        print(user_list_serializer)
        return JsonResponse(user_list_serializer.data, safe=False)

    @api_view(["POST"])
    def signup(request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'error': '회원정보가 저장되지 않았습니다'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

    @api_view(["PUT"])
    @authentication_classes([JSONWebTokenAuthentication])
    @permission_classes([IsAuthenticated])
    def user_modify(request):
        
        user = User.objects.get(username = request.data["username"])

        if user:
            user_serializer = UserSerializer(user, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return JsonResponse(user_serializer.data, safe=False)
        return Response({'error': '회원정보가 저장되지 않았습니다'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        