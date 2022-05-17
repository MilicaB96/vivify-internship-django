from re import U
from urllib import request
from django.shortcuts import render
from rest_framework.mixins import RetrieveModelMixin,ListModelMixin
from django.contrib.auth.models import User
from userapp.serializer import UserSerializer
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import MyTokenObtainPairSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import  IsAuthenticated,IsAdminUser
from django.db.models import Q

# Create your views here.
class UserViewSet(viewsets.GenericViewSet, RetrieveModelMixin, ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    @action(detail=False, methods=['get'], url_path='me', url_name='me',
    permission_classes = [IsAuthenticated])
    def get_user_data(self, request):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
    def get_queryset(self):
        name = self.request.query_params.get('name')
        if name is not None:
            self.queryset = self.queryset.filter(Q(first_name=name) | Q(last_name=name))
        return self.queryset
        
    
class LoginViewSet(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer
    