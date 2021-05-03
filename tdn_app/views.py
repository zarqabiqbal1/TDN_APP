from django.shortcuts import render
from rest_framework import  generics
from tdn_app.models import UserModel
from tdn_app.serializer import UserSerializer


class UserView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
