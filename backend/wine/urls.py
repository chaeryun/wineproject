from django.urls import path
from . import views

urlpatterns = [
    path('get_wine_data/<int:wine_id>/', views.get_wine_data),
    path('get_wine_list/', views.get_wine_list),
    path('update_wine_data/', views.update_wine_data),
    path('add_wine_wishlist/<int:wine_id>/<int:user_id>/', views.add_wine_wishlist),
    path('latest_wine_list/<int:user_id>/', views.latest_wine_list), #최근에 내가 찜한 와인 리스트
    path('latest_wine_totallist/<int:user_id>/', views.latest_wine_totallist),

    path('recommand/latest_wishlist/<int:user_id>/', views.reco_wishlist), #찜 기반 와인 추천 ?????
    path('recommand/similar_wine/<int:wine_id>/', views.reco_similar_wine), #단일 와인-> 유사와인 추천
    path('recommand/reviews/<str:color>/', views.reco_color_reviewbased), #사람들이 많이 찾은 와인
    path('recommand/color_score/<str:color>/', views.reco_color_score), #빈티지 점수 기반 추천 와인

    path('recommand/onlyfood/<str:food>/', views.reco_onlyfood),
    path('recommand/categorize/<str:country>/<str:grapes>/<int:min_price>/<int:max_price>/<int:taste>/<int:dry>/<int:soft>/<int:light>/<int:smooth>/', views.reco_categorize),
]
