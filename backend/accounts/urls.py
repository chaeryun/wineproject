from django.urls import path
from .views import AccountManagement
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('signup/', AccountManagement.signup),
    path('login/', obtain_jwt_token),
]