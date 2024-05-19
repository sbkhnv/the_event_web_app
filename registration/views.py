from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import Registration, LoginForm
from django.core.mail import send_mail
from django.conf import settings
from django.core.exceptions import ValidationError

def register_view(request):
    form = Registration()
    if request.method == "POST":
        # user_n = request.POST['username']
        # passw = request.POST['passw']
        # c_passw = request.POST['c_passw']

        # data = {'username': user_n, 'password': passw, 'confirm_password': c_passw}
        # print(user_n, passw, c_passw)
        form = Registration(request.POST)
        if form.is_valid():
            del form.cleaned_data["confirm_password"]
            # email = form.cleaned_data["email"]
            # message = "You have registered your account."
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            # send_mail(
            #     'Registration', message, 'settings.EMAIL_HOST_USER', [email], fail_silently=False)
            return redirect("login")

    return render(request, "register.html", {"form": form})


def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = (authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']))

        if user is not None:
            login(request, user)
            return redirect("home")
        form.add_error("password", "Username yoki parol noto\'g\'ri ")

    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")