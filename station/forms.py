from django import forms
from django.core.validators import RegexValidator

my_validator = RegexValidator(r'^[0-9]*$','ZIP MUST BE 5 NUMBERS!!')

class ZipForm(forms.Form):

    zip = forms.CharField(max_length=5,validators=[my_validator])
