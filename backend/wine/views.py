from ntpath import join
from urllib import response
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view

from .models import Userlikewine, Wine
from .serializers import WineSerializer

from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import json
# Create your views here.

#-------------------와인 기본 API---------------------------------
@api_view(['GET'])
@permission_classes([AllowAny]) 
#단일 와인 정보 페이지를 위한 개별와인정보 검색 API
def get_wine_data(request):
    print(request.data['wine'])
    try: 
        wine = Wine.objects.get(wine = request.data["wine"])
        wine_serializer = WineSerializer(wine)
        return Response(wine_serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({'와인이 없습니다'}, status=status.HTTP_200_OK)

#전체 와인 리스트 반환
@api_view(["GET"])
@permission_classes([AllowAny])
def get_wine_list(request):
    wine_list = Wine.objects.all()
    print(wine_list)
    wine_list_serializer = WineSerializer(wine_list, many=True)
    return JsonResponse(wine_list_serializer.data, safe=False)

@api_view(["POST"])
@permission_classes([AllowAny])#후에 권한설정 변경 필요
def update_wine_data(request):
    f = open('../dataset/wine.json', 'r', encoding='UTF-8')
    data = json.load(f)
    for wine in data:
        new_wine_data = Wine()

        new_wine_data.wine = wine["wine"]
        new_wine_data.color = wine["color"]
        new_wine_data.alcohol = wine["alcohol"]
        new_wine_data.image = wine["image"]

        if wine["winery"] == "": new_wine_data.winery = "Unknown Winery"
        else: new_wine_data.winery = wine["winery"]

        try: new_wine_data.location = wine["location"]
        except: new_wine_data.location = "Unknown Location"

        if wine["price"] == "": new_wine_data.price = "-1"
        else: new_wine_data.price = wine["price"]

        if wine["light"] == "":new_wine_data.light = -1
        else: new_wine_data.light = wine["light"]

        if wine["smooth"] == "": new_wine_data.smooth = -1
        else: new_wine_data.smooth = wine["smooth"]
        
        if wine["dry"] == "": new_wine_data.dry = -1
        else: new_wine_data.dry = wine["dry"]

        if wine["soft"] == "": new_wine_data.soft = -1
        else: new_wine_data.soft = wine["soft"]        
        
        if wine["gentle"] == "": new_wine_data.gentle = -1
        else: new_wine_data.gentle = wine["gentle"]                

        new_wine_data.taste = ", ".join(wine["taste"])
        new_wine_data.food = ", ".join(wine["food"])
        new_wine_data.grapes = ", ".join(wine["grapes"])
        
        new_wine_data.save()
    
    return Response({"DB저장완료"}, status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([AllowAny])
def add_wine_wishlist(request, wine_name):
    if Userlikewine.objects.filter(wine = wine_name).filter(user = request.user).exists():
        like = get_object_or_404(Userlikewine, wine = wine_name, user=request.user), 
        like.delete()
        return Response({"좋아요 취소 완료"}, status=status.HTTP_202_ACCEPTED)

    else:
        wine = get_object_or_404(Wine, wine=wine_name)
        instance = Userlikewine()
        instance.wine = wine
        instance.user = request.user
        instance.save()
        return Response({"좋아요 완료"}, status=status.HTTP_202_ACCEPTED)

#------------------------------날씨 관련----------------------------------