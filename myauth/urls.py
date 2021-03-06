from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = 'myauth'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]
