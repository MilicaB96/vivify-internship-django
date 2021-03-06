from django.urls import path,re_path
from rest_framework import routers
from .views import LoginViewSet, UserProfile, UserViewSet 

userRouter = routers.SimpleRouter()
userRouter.register(r'user', UserViewSet)

userApiView = [
    path('login',LoginViewSet.as_view(), name = 'login'),
    path('user/<int:user_id>/', UserProfile.as_view(), name ='profile')
]
