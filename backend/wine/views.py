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
def get_wine_data(request, wine_id):
    try: 
        wine = Wine.objects.get(wine_id = wine_id)
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

    #검색해야 하는 데이터들
    # wine_id / wine  / winery / country / location 
    # image   / color / price  / light   / smooth
    # dry     / soft  / gentle / taste   / food 
    # grapes  / alcohol / likes /
    for index in range(2850):
        wine = Wine()
        index_str = str(index)

        wine.wine_id = data["wine_id"][index_str]
        wine.wine = data["wine"][index_str]
        wine.winery = data["winery"][index_str]
        wine.country = data["country"][index_str]
        wine.location = data["location"][index_str]
        wine.color = data["color"][index_str]

        wine.image = data["image"][index_str]
        wine.price = data["price"][index_str]
        wine.light = data["light"][index_str]
        wine.smooth = data["smooth"][index_str]
        wine.dry = data["dry"][index_str]
        wine.soft = data["soft"][index_str]

        wine.gentle = data["gentle"][index_str]
        wine.taste = data["taste"][index_str]
        wine.food = ", ".join(data["food"][index_str])
        wine.grapes = ", ".join(data["grapes"][index_str])
        wine.alcohol = data["alcohol"][index_str]

        wine.save()
    
    return Response({"DB저장완료"}, status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([AllowAny])
def add_wine_wishlist(request, wine_id):
    if Userlikewine.objects.filter(wine_id = wine_id).filter(user = request.user).exists():
        wine = get_object_or_404(Wine, wine_id=wine_id)
        wine.likes -= 1
        wine.save()
        like = get_object_or_404(Userlikewine, wine_id = wine_id, user=request.user),
        like.delete()
        
        return Response({"좋아요 취소 완료"}, status=status.HTTP_202_ACCEPTED)

    else:
        wine = get_object_or_404(Wine, wine_id=wine_id)

        instance = Userlikewine()
        instance.wine = wine
        instance.user = request.user
        instance.save()

        wine.likes += 1
        wine.save()

        return Response({"좋아요 완료"}, status=status.HTTP_202_ACCEPTED)
