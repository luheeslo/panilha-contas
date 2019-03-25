from rest_framework import serializers
from .models import Register


class RegisterSerializer(serializers.ModelSerializer):

    """Docstring for RegisterSerializer. """

    class Meta:
        model = Register
        fields = ('name', 'amount')
