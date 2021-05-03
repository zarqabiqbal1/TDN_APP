from abc import ABC

from rest_framework import serializers
from tdn_app.models import UserModel


class UserSerializer(serializers.Serializer):

    user_id = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(required=True)
    date = serializers.DateField(required=True)

    class Meta:
        model = UserModel
        fields = '__all__'

    def create(self, validated_data):
        email_check = UserModel.objects.filter(email = validated_data['email'])
        try :
            email_check[0]
            raise serializers.ValidationError('User already exist with this User Id')
        except IndexError:
            user =  UserModel(**validated_data)
            user.save()
            return user