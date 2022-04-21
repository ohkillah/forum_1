import email
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import random
from .mailsender import send_email


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect("/")

def login_view(request: HttpRequest) -> HttpResponse:
    context = {"message": "", "email": ""}
    if request.method == "POST":
        existingUser = User.objects.filter(
            email=request.POST.get("email", "")).first()
        if existingUser is None:
            context["message"] = "Incorrect email or password"
            context["email"] = request.POST.get("email", "")
            return render(request, "login.html", context=context)
        user = authenticate(
            username=existingUser.username,
            password=request.POST.get("password", ""),
        )
        if user is not None:
            login(request, user=user)
            return redirect("/")
        context["email"] = request.POST.get("email", "")
        context["message"] = "Incorrect login or password"

    return render(request, "login.html", context=context)


def register_view(request: HttpRequest) -> HttpResponse:
    context = {"message": "", "username": ""}
    if request.method == "POST":
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")
        username = request.POST.get("username", "")
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")
        email = request.POST.get("email", "")
        error = ""
        if username == "":
            error = "Please enter username"
        if email == "":
            error = "Please enter email"
        if password1 == "":
            error = "Please enter password"
        if password1 != password2:
            error = "Passwords do not match"
        if User.objects.filter(username=username).count() > 0:
            error = "User already exists. Please login."
        if User.objects.filter(email=email).count() > 0:
            error = "User with similar email already exists. Please login."
        if error == "":
            user = User.objects.create_user(username=username, password=password1, email=email,
                                            first_name=first_name, last_name=last_name, is_superuser=False, is_staff=False)
            login(request, user)
            return redirect("/")

        context["username"] = request.POST.get("username", "")
        context["message"] = error

    return render(request, "register.html", context=context)


def forgot_password_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        email = request.POST.get("email", "")
        if email != "":
            try:
                print('Try to find user with email: ' + email)
                user = User.objects.get(email=email)
                new_password = "".join(
                    [random.choice(list("ABCDEabcde0123456789")) for i in range(6)])
                user.set_password(new_password)
                user.save()
                text = f"Your new password is this: {new_password}"
                send_email.delay(
                    email=email,
                    text=text,
                    subject="Password Recovery",
                )
                print('Email sent')
                return redirect("/forgot_password_success")
            except ObjectDoesNotExist:
                print("Some hacker tried this email", email)
                return redirect("/forgot_password_success")
    return render(request, "forgot_password.html")


def forgot_password_success_view(request: HttpRequest) -> HttpResponse:
    print("Forgot password success view")
    return render(request, "forgot_password_success.html")
