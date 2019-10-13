from rest_framework import viewsets
from user.api.serializer import UserSerializers, GroupSrializer
from django.contrib.auth.models import User, Group
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .permissions import IsOwnerOrAdminOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all().order_by('-date_joined')
    permission_classes = [IsAuthenticatedOrReadOnly,
                          IsOwnerOrAdminOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSrializer
    queryset = Group.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
