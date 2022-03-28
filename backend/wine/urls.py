from django.urls import path
from . import views

urlpatterns = [
    path('get_wine_data/', views.get_wine_data),
    path('get_wine_list/', views.get_wine_list),
    path('update_wine_data/', views.update_wine_data),
]
