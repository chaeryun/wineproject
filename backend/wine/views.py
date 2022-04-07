from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view

from .models import Userlikewine, Wine
from accounts.models import User
from .serializers import UserlikewineSerializer, WineSerializer

from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import json
import math
import random
from reco.algo1 import reco_color_average, reco_color_reviews, reco_likes, weather
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
def add_wine_wishlist(request, wine_id, username):
    user = User.objects.get(username=username)
    user_id = user.id

    if Userlikewine.objects.filter(wine_id = wine_id).filter(user_id = user_id).exists():
        wine = get_object_or_404(Wine, wine_id=wine_id)
        wine.likes -= 1
        wine.save()

        like = Userlikewine.objects.get(wine_id=wine_id, user_id=user_id)
        like.delete()
        
        return Response({"좋아요 취소 완료"}, status=status.HTTP_202_ACCEPTED)

    else:
        wine = get_object_or_404(Wine, wine_id=wine_id)

        instance = Userlikewine()
        instance.wine = wine
        instance.user_id = user_id
        instance.save()

        wine.likes += 1
        wine.save()

        return Response({"좋아요 완료"}, status=status.HTTP_202_ACCEPTED)

#----------------------와인 추천 API-------------------------------

@api_view(["GET"])
@permission_classes([AllowAny])
def latest_wine_list(request, user_id):
    wines = Userlikewine.objects.filter(user_id = user_id).order_by('-created_at')[:5]
    serializer = UserlikewineSerializer(wines, many=True)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

@api_view(["GET"])
@permission_classes([AllowAny])
def latest_wine_totallist(request, user_id):
    wines = Userlikewine.objects.filter(user_id = user_id).order_by('-created_at')
    serializer = UserlikewineSerializer(wines, many=True)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

@api_view(["GET"])
@permission_classes([AllowAny])
def reco_similar_wine(request, wine_id):
    wine_list = reco_likes(wine_id)
    wines = Wine.objects.filter(wine_id__in=random.sample(wine_list, 3))
    wineserializers = WineSerializer(wines, many=True)
    return Response(wineserializers.data, status=status.HTTP_202_ACCEPTED)


@api_view(["GET"])
@permission_classes([AllowAny])
def reco_wishlist(request, user_id):
    wines = Userlikewine.objects.filter(user_id = user_id)[:5]
    reds = []
    port = []
    spark = []
    white = []
    rose = []
    matrix = [0, 0, 0, 0, 0]
    wine_matrix = [reds, port, spark, white, rose]
    for wine in wines:
        id_list = reco_likes(wine.wine.wine_id, n=5)
        if wine.wine.color == "red":
            matrix[0] += 1
            for id in id_list:
                wine_matrix[0].append(id)
        elif wine.wine.color == "port":
            matrix[1] += 1
            for id in id_list:
                wine_matrix[1].append(id)
        elif wine.wine.color == "sparkling":
            matrix[2] += 1
            for id in id_list:
                wine_matrix[2].append(id)
        elif wine.wine.color == "white":
            matrix[3] += 1
            for id in id_list:
                wine_matrix[3].append(id)
        else:
            matrix[4] += 1
            for id in id_list:
                wine_matrix[4].append(id)

    if sum(matrix) < 5:
        wine_list = wine_matrix[0] + wine_matrix[1] + wine_matrix[2] + wine_matrix[3] + wine_matrix[4]
        wines = Wine.objects.filter(wine_id__in=random.sample(wine_list, 5))
        wineserializers = WineSerializer(wines, many=True)
        return Response(wineserializers.data, status=status.HTTP_200_OK)
    else:
        result_list = []
        i = 0
        while len(result_list) < 5:
            
            if matrix[i]:
                matrix[i] -= 1
                result_list.append(random.choice(wine_matrix[i]))
            if i == 4:
                i = 0
            i += 1
        wines = Wine.objects.filter(wine_id__in=result_list)
        wineserializers = WineSerializer(wines, many=True)
        return Response(wineserializers.data, status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([AllowAny])
def reco_color_reviewbased(request, color):
    result_list = reco_color_reviews(color, 5)
    wines = Wine.objects.filter(wine_id__in=random.sample(result_list, 5))
    wineserializers = WineSerializer(wines, many=True)
    return Response(wineserializers.data, status=status.HTTP_200_OK)        

@api_view(["GET"])
@permission_classes([AllowAny])
def reco_color_score(request, color):
    result_list = reco_color_average(color, 5)
    wines = Wine.objects.filter(wine_id__in=random.sample(result_list, 5))
    wineserializers = WineSerializer(wines, many=True)

    return Response(wineserializers.data, status=status.HTTP_200_OK)        

@api_view(["GET"])
@permission_classes([AllowAny])
def reco_onlyfood(request, food):
    wines = Wine.objects.filter(food__contains=food)
    wineserializers = WineSerializer(wines, many=True)
    return Response(wineserializers.data, status=status.HTTP_200_OK)


#path('recommand/categorize/<str:country>/<str:grapes>/<int:min_price>/<int:max_price>/<int:taste>/<int:dry>/<int:soft>/<int:light>/<int:smooth>/', views.reco_categorize),
@api_view(["GET"])
@permission_classes([AllowAny])
def reco_categorize(request, country, grapes, min_price, max_price, taste, dry, soft, light, smooth):

    def get_min_max(number):
        sample_number = math.floor(number)
        if sample_number % 2:
            return float((sample_number - 1)*2), float(sample_number * 2)
        else:
            return float((sample_number)), float((sample_number+1)*2)      

    if dry: dry_min, dry_max = get_min_max(dry)
    if soft: soft_min, soft_max = get_min_max(soft)
    if light: light_min, light_max = get_min_max(light)
    if smooth: smooth_min, smooth_max = get_min_max(smooth)

    wines = Wine.objects.all()
    if country != 'all': wines = wines.filter(country=country)
    if grapes != 'all': wines = wines.filter(grapes__contains=grapes)
    wines = wines.filter(price__range=(min_price, max_price))
    if taste != 'all': wines = wines.filter(taste__contains=taste)
    if dry: wines = wines.filter(dry__range=(dry_min, dry_max))
    if soft: wines = wines.filter(soft__range=(soft_min, soft_max))
    if light: wines = wines.filter(light__range=(light_min, light_max))
    if smooth: wines = wines.filter(smooth__range=(smooth_min, smooth_max))

    #wines = Wine.objects.filter(country=country).filter(grapes__in=grapes).filter(price__gte=min_price).filter(price__lte=max_price).filter(taste__in=taste).filter(dry__lte=dry_max).filter(dry__gte=dry_min).filter(soft__lte=soft_max).filter(soft__gte=soft_min).filter(light__lte=light_max).filter(light__gte=light_min).filter(smooth__lte=smooth_max).filter(smooth__gte=smooth_min)
    wineserializers = WineSerializer(wines, many=True)
    return Response(wineserializers.data, status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([AllowAny])
def reco_vintage(request, year):
    wine_lists = weather(year)
    wines = Wine.objects.filter(wine_id__in=wine_lists)
    wineserializers = WineSerializer(wines, many=True)
    return Response(wineserializers.data, status=status.HTTP_200_OK)
    