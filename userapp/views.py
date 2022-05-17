from argparse import Action
from urllib import response
from django.shortcuts import render
from rest_framework.mixins import RetrieveModelMixin
from django.contrib.auth.models import User
from userapp.serializer import UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import MyTokenObtainPairSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet,RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    

class LoginViewSet(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer
    
    