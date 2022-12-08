from django.contrib.auth.models import User
from rest_framework import serializers
from Auth.models import UserInfo

class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = ['username' , 'name','email' , 'college' , 'clg_city' , '']


class RegistrationSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ['username','password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):

        password = self.validated_data['password']


        if User.objects.filter(email=self.validated_data['username']).exists():
            raise serializers.ValidationError({'error': 'Username already exists!'})

        account = User(username=self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account