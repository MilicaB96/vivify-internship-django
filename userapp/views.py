from django.shortcuts import render
from rest_framework.mixins import RetrieveModelMixin
from django.contrib.auth.models import User
from userapp.serializer import UserSerializer
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import MyTokenObtainPairSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import  IsAuthenticated,IsAdminUser

# Create your views here.
class UserViewSet(viewsets.ModelViewSet,RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    @action(detail=False, methods=['get'], url_path='me', url_name='me',
    permission_classes = [IsAuthenticated])
    def get_user_data(self, request):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

class LoginViewSet(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer
    