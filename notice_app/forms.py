from .models import Board
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AddBoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('title', 'category', 'description', 'image', 'price', 'is_related_price', 'author_name', 'author_number',)

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')