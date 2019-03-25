from django.db import models


class Register(models.Model):

    """Docstring for Register. """

    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
