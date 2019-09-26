from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='blog-about'),
    path('', views.PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail-post'),
    path('post/create/', views.PostCreateView.as_view(), name='create-post'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='update-post'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete-post'),
    path('post/<str:username>/', views.UserPostListView.as_view(), name='user-posts'),
]
