#forms.py
from django import forms
from my_bbs.models import Board, Comment

from django.forms import ModelForm
from django.contrib.auth.models import User







class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'contents']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['contents']


class SignupForm(ModelForm):
    password_check = forms.CharField(max_length=200, widget=forms.PasswordInput())
    # widget=forms.PasswordInput()은 입력 양식을 password로 지정한다고 한다.
    field_order = ['username', 'password', 'password_check', 'last_name', 'first_name', 'email']
    # 만들어지는 입력양식의 순서

    class Meta:
        model = User
        widgets = {'password': forms.PasswordInput}
        fields = ['username', 'password', 'last_name', 'first_name', 'email']


class SigninForm(ModelForm):
    class Meta:
        model = User
        widgets = {'password': forms.PasswordInput}
        fields = ['username', 'password']



