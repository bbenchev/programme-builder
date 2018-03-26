from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Programme


ACCREDITATIONS_CHOICES = (
    ("IET", "IET"),
    ("BCS", "BCS"),
    ("QAA", "QAA")
)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")


class ProgrammeForm(forms.ModelForm):
    modules = forms.MultipleChoiceField()
    accreditations = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=ACCREDITATIONS_CHOICES
    )

    class Meta:
        model = Programme
        fields = ["name", "ucas_code", "level", "years", "accreditations", "modules"]