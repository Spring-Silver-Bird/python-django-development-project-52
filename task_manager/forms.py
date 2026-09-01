from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'username': 'Имя пользователя',
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username']
        labels = {'first_name': 'Имя','last_name': 'Фамилия','username': 'Имя пользователя'}
