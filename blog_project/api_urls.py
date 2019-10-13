from django.urls import path, include
from user.api.views import UserViewSet, GroupViewSet
from blog.api.views import PostViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)
router.register('posts', PostViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
