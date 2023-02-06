from django import forms
from .models import CustomUser

class UserCreateForm(forms.Form):
    attrs = {
        "type": "password"
    }

    username = forms.CharField(max_length=128)

    first_name = forms.CharField(max_length=128)
    last_name = forms.CharField(max_length=128)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.TextInput(attrs=attrs))
    # password = forms.PasswordInput()

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture')

# class UserLoginForm(forms.Form):
#     username = forms.CharField(max_length=128)
#     password = forms.CharField(widget=forms.TextInput(attrs={"type": "password"}), max_length=128)





