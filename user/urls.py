from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='user-register'),
    path('profile/<str:username>/', views.profile, name='user-profile'),
    path('login/', views.UserLoginView.as_view(), name='user-login'),
    path('logout/', views.UserLogoutView.as_view(), name='user-logout'),
    path('password-reset/', views.UserPasswordResetView.as_view(),
         name='password-reset'),
    path('password-reset/done/', views.UserPasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset/complete/', views.UserPasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

]
