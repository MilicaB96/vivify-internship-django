from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(required = True, max_length = 150)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    email = serializers.EmailField(required=True,max_length = 254)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
