from django import forms
TYPE_CHOICES = (
    (1, "entrada"),
    (2, "saida"),
)


class RegisterForm(forms.Form):

    type = forms.ChoiceField(choices=TYPE_CHOICES, required=True)
    name = forms.CharField(max_length=100, required=True)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['type'] == 'entrada':
            cleaned_data['amount'] = abs(cleaned_data['amount'])
        else:
            cleaned_data['amount'] = -cleaned_data['amount']
