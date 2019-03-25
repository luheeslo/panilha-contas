from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class LoginView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def post(self, request):
        user = User.objects.filter(email=request.data['email']).first()
        if user:
            if check_password(request.data.get('password'), user.password):
                login(request, user)
                return Response({'login': 'OK'})
        raise ValidationError('Incorrect email or password.')


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response()
