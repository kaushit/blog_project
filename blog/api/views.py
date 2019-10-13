from rest_framework import viewsets
from blog.api.serializer import PostSerializers
from blog.models import Post
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrAdminOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializers
    queryset = Post.objects.all().order_by('-date_posted')
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrAdminOrReadOnly]
