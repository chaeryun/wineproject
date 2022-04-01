from distutils.log import error
from django.http import JsonResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .models import User
from .serializers import UserBodySerializer, UserSerializer

from drf_yasg.utils import swagger_auto_schema
# Create your views here.

class AccountManagement(APIView):
    #전체 유저 데이터 조회
    @api_view(["GET"])
    @permission_classes([AllowAny])
    def get_user_list(request):
        user_list = User.objects.all()
        user_list_serializer = UserSerializer(user_list, many=True)
        print(user_list_serializer)
        return JsonResponse(user_list_serializer.data, safe=False)


    #중복확인 및 프로필 검색을 위한 단일 유저 데이터 조회
    @api_view(["GET"])
    @permission_classes([AllowAny])
    def get_user(request, user_name):
        try: 
            user = User.objects.get(username = user_name)
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'유저가 없습니다.'}, status=status.HTTP_200_OK)
        

    #회원정보 저장(회원가입)
    @api_view(["POST"])
    @permission_classes([AllowAny])
    #@swagger_auto_schema(query_serializer=UserBodySerializer)
    def signup(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'error': '회원정보가 저장되지 않았습니다'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

    #회원정보 수정
    @api_view(["PUT"])
    #@authentication_classes([JSONWebTokenAuthentication]) #전부 마무리되면 권한설정 on
    #@permission_classes([IsAuthenticated]) #전부 마무리되면 권한설정 on
    @permission_classes([AllowAny])
    def user_modify(request):
        user = User.objects.get(username = request.data["username"])
        user_serializer=UserSerializer(user, data=request.data)
        
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, safe=False)
        return Response({'error': '회원정보가 저장되지 않았습니다'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        
