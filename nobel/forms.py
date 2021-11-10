from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from nobel.models import StudentForm

genderChoose=[(0,'Male'),(1,'Female'),(2,'Others')]
class NameForm(forms.Form):
    studentName = forms.CharField(label='Student Name', max_length=100)
    gender=forms.ChoiceField(choices=genderChoose,label='Gender')