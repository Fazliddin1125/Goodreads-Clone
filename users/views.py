from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from users.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserCreateForm, UserUpdateForm
from django.contrib import messages


# Create your views here.

class RegisterView(View):
    def get(self, requset):
        create_form = UserCreateForm()
        context = {
            "form": create_form
        }
        return render(requset, 'users/register.html', context)

    def post(self, request):
        create_form = UserCreateForm(request.POST)

        if create_form.is_valid():
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']

            user = CustomUser.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email
            )

            user.set_password(password)
            user.save()



            return redirect('login')
        else:
            context = {
                "form": create_form
            }
            return render(request, 'users/register.html', context)


class LoginView(View):
    def get(self, requset):

        login_form = AuthenticationForm()
        context = {
            'form': login_form
        }
        return render(requset, 'users/login.html', context)

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        context = {
            'form': login_form
        }

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, "You have successfuly logged in.")
            return redirect('list')

        else:
            return render(request, 'users/login.html', context)


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):

        return render(request, 'users/profile.html', {'user': request.user})

class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return redirect('landing_page')


class ProfileEditView(LoginRequiredMixin, View):
    def get(self, request):
        edit_form = UserUpdateForm(instance=request.user)
        return render(request, 'users/profile_edit.html', {'form': edit_form})

    def post(self, request):
        edit_form = UserUpdateForm(
            instance=request.user,
            data=request.POST,
            files=request.FILES
        )
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, "You have successfully updated your profile.")
            return redirect('profile')
        else:
            return render(request, 'users/profile_edit.html', {'form': edit_form})
