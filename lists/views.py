from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser

from .models import Register
from .serializers import RegisterSerializer
from .forms import RegisterForm


class RegisterView(generics.ListAPIView):

    """Get all registers.

       Optional queries: order_by/sorted_by
       Examples:
           http://url:port/lists/registers
           http://url:port/lists/registers/?order_by=name&sorted_by=a
           http://url:port/lists/registers/?order_by=amount&sorted_by=d
    """
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

    """Create a register.
       Type with value 1 == input
       Type with value 2 == output
       Examples:
           http --form POST http://lhel.pythonanywhere.com/lists/create_register/ type=1 name=Teste2 amount=100.00 'Authorization: Token token_example'
           httpie --form post http://url:port/lists/create_register type=2 name=Teste2 amount=100.00

    """

    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request, format=None):
        form = RegisterForm(request.POST)
        if form.is_valid():
            r = Register.objects.create(name=form.cleaned_data['name'],
                                        amount=form.cleaned_data['amount'])
            return Response(RegisterSerializer(r).data, status=201)
        else:
            return Response({'errors': form.errors}, status=400)
