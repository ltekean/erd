from django.urls import path, include
from accounts import views

urlpatterns = [
    path('signup/', views.signup, name='sign_up' ),
    path('login/', views.user_login, name='user_login'),
]