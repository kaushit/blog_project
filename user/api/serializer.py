from rest_framework import serializers
from django.contrib.auth.models import User, Group


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email']


class GroupSrializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
