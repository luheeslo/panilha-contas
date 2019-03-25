from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser

from .models import Register
from .serializers import RegisterSerializer
from .forms import RegisterForm


class RegisterView(generics.ListAPIView):

    """Docstring for RegisterView. """
    serializer_class = RegisterSerializer

    def get_queryset(self):
        queryset = Register.objects.all()
        order_by = self.request.query_params.get('order_by', None)
        sort_by = self.request.query_params.get('sort_by', 'a')
        if order_by is not None:
            if sort_by == 'a':
                return queryset.order_by(order_by)
            else:
                return queryset.order_by("-" + order_by)
        else:
            return queryset


class CreateRegisterView(APIView):

    """Docstring for CreateRegisterView. """

    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request, format=None):
        form = RegisterForm(request.POST)
        if form.is_valid():
            r = Register.objects.create(name=form.cleaned_data['name'],
                                        amount=form.cleaned_data['amount'])
            return Response(RegisterSerializer(r).data, status=201)
        else:
            return Response({'errors': form.errors}, status=400)
