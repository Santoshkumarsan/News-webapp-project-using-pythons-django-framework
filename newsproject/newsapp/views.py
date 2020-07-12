from django.shortcuts import render, redirect, HttpResponse
from newsapp.models import mainnews
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView


def news_home(request):
   mainnewsed = mainnews.objects.all()
   my_dict = {'mainnewsed': mainnewsed}

   return render(request, 'newsapp/index.html', my_dict)


@login_required
def news_2ndhome(request):
    mainnewsed = mainnews.objects.all()
    my_dict = {'mainnewsed': mainnewsed}

    return render(request, 'newsapp/index2.html', my_dict)


def signupsystem(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        #print("user created")
        return redirect('/')
    else:
        return render(request, 'newsapp/signup.html')


def handlelogout(request):
    return HttpResponse('handle logout')


@login_required
def firstnews(request):
    newse = mainnews.objects.all()
    my_dict = {'newse': newse}
    return render(request, 'newsapp/news1.html', my_dict)


@login_required
def secondnews(request):

    newse = mainnews.objects.all()
    my_dict = {'newse': newse}

    return render(request, 'newsapp/news2.html', my_dict)


@login_required
def thirdnews(request):

    newse = mainnews.objects.all()
    my_dict = {'newse': newse}

    return render(request, 'newsapp/news3.html', my_dict)


@login_required
def fourthnews(request):

    newse = mainnews.objects.all()
    my_dict = {'newse': newse}

    return render(request, 'newsapp/news4.html', my_dict)


@login_required
def fifthnews(request):

    newse = mainnews.objects.all()
    my_dict = {'newse': newse}

    return render(request, 'newsapp/news5.html', my_dict)


@login_required
def sixthnews(request):

    newse = mainnews.objects.all()
    my_dict = {'newse': newse}

    return render(request, 'newsapp/news6.html', my_dict)


@login_required
def seventhnews(request):

    newse = mainnews.objects.all()
    my_dict = {'newse': newse}

    return render(request, 'newsapp/news7.html', my_dict)


@login_required
def eightthnews(request):

    newse = mainnews.objects.all()
    my_dict = {'newse': newse}

    return render(request, 'newsapp/news8.html', my_dict)
