from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Register
from .serializers import RegisterSerializer


class RegisterView(APIView):

    """Docstring for RegisterView. """

    def get(self, request):
        registers = Register.objects.all()
        serializer = RegisterSerializer(registers, many=True)
        return Response(serializer.data)
