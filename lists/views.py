from rest_framework import generics

from .models import Register
from .serializers import RegisterSerializer


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
