from urllib import response
from django.shortcuts import render
from rest_framework.mixins import RetrieveModelMixin
from django.contrib.auth.models import User
from userapp.serializer import UserSerializer
from rest_framework.viewsets import GenericViewSet
# Create your views here.
class UserViewSet(GenericViewSet,RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

