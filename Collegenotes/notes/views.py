from django.shortcuts import render, HttpResponse, redirect
from .models import Signupinfo, Uploadnotes
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def about(request):
    return render(request, 'About.html')


def index(request):

    return render(request, 'index.html')


def contact(request):
    return render(request, 'ContactUs.html')


def login1(request):
    return render(request, 'Login.html')


def signup(request):
    return render(request, 'Signup.html')


def signupinfohandle(request):
    if request.method == 'POST':
        fname = request.POST["firstname"]
        lname = request.POST["lastname"]
        emailview = request.POST["emailid"]
        classstud = request.POST["classofstud"]
        college = request.POST["college"]
        password = request.POST["password"]
        confpasswd = request.POST["cnfpwd"]

        if not fname[0].isupper() and not lname[0].isupper():
            messages.error(request, "First letter of First Name and Last Name should be Capital")
            return render(request, 'Signup.html')

        if not len(password) and len(confpasswd) > 8:
            messages.error(request, "Password length should be maximum 8 characters")
            return render(request, 'Signup.html')

        if password != confpasswd:
            messages.error(request, "Password didn't match")
            return render(request, 'Signup.html')

        try:
            user = User.objects.create_user(username=emailview, password=password, first_name=fname, last_name=lname)
            user.save()
            Signupinfo.objects.create(user=user, studentclass=classstud, studentcollege=college,
                                      confpassword=confpasswd)

            messages.success(request, "Account Created")
            return render(request, 'Login.html')

        except:
            messages.error(request, "Something went wrong")
            return render(request, 'Signup.html')


from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def loginhandle(request):
    if request.method == 'POST':
        email = request.POST["emailid"]
        passwordlogin = request.POST["pwd"]

        user = authenticate(request, username=email, password=passwordlogin)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful!!")
            return render(request, 'Afterlogin.html')
        else:
            messages.error(request, "Invalid Email or Password!!")
            return render(request, 'Login.html')

    return HttpResponse("404-Not found")


def logouthandle(request):
    logout(request)
    messages.success(request, "Logout Successful!!")
    return redirect('index')


def csfy(request):
    if request.user.is_authenticated:
        files = Uploadnotes.objects.all()
        return render(request, 'csfy.html', {'files': files})
    else:
        return HttpResponse('Error-please login and try again')


def cssy(request):
    if request.user.is_authenticated:
        files = Uploadnotes.objects.all()
        return render(request, 'cssy.html', {'files': files})
    else:
        return HttpResponse('Error-please login and try again')


def csty(request):
    if request.user.is_authenticated:
        files = Uploadnotes.objects.all()
        return render(request, 'csty.html', {'files': files})
    else:
        return HttpResponse('Error-please login and try again')
