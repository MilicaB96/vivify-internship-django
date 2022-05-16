# from django.urls import path
from rest_framework import routers
from .views import UserViewSet
userRouter = routers.SimpleRouter()
userRouter.register(r'user', UserViewSet)
# userApiView = [
#     url('user',UserViewSet, name = 'user')
# ]
