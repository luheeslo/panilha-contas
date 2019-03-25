from django.urls import path
from . import views

app_name = 'lists'
urlpatterns = [
    path('registers/', views.RegisterView.as_view(), name='registers'),
]
