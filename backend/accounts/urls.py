from django.urls import path
from .views import AccountManagement
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('get_user/<str:user_name>/', AccountManagement.get_user),
    path('get_user_list/', AccountManagement.get_user_list),
    path('signup/', AccountManagement.signup),
    path('login/', obtain_jwt_token),
    path('user_modify/', AccountManagement.user_modify)
]