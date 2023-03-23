
from importlib.resources import contents
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from home.models import Blocks
from .models import Blocks
from .models import Unblocks
from home.models import Unblocks
from django.contrib.auth.models import User
import sys
import platform

#For Bloking

#hostpath = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websites = []

if platform.system() == 'Windows':
    hostpath = "C:\Windows\System32\drivers\etc\hosts"
elif platform.system() == "Linux" or platform.system() == "darwin":
    hostpath = "/etc/hosts"


def index(request):
    return render(request , 'home.html')

def About(request):
    return render(request , 'About.html')

def step(request):
    return render(request , 'step.html')

def contact(request):
    return render(request , 'contact.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your Account has been created")

        return HttpResponseRedirect('step')
    return render(request , 'register.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(username=username, password = pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return HttpResponseRedirect('options', {'fname':fname})
        else:
            messages.error(request, "Bad Credential")
    return render(request , 'Login.html')

def logout_user(request):
    auth_logout(request)
    return HttpResponseRedirect('/')

    

def block(request):
    if request.method == "POST":
        blocked = request.POST.get('blocked')
        if blocked not in websites:
            #----
            block = Blocks(blocked=blocked, date=datetime.today(), time = datetime.now())
            block.save()
            #----
            name = blocked[4:]
            websites.append(blocked)
            websites.append(name)
            websites.append("m."+name)

        god()                      # code to block
    return render(request , 'block.html')


def unblock(request):
    if request.method == "POST":
        unblocked = request.POST.get('unblocked')
        if unblocked in websites:
            #----
            unblock = Unblocks(unblocked=unblocked, date=datetime.today(), time = datetime.now())
            unblock.save()
            #----
            name = unblocked[4:]
            websites.remove(unblocked)
            websites.remove(name)
            websites.remove("m."+name)
        god()                    # code to unblock
    return render(request , 'unblock.html')

def clearing(request):
    websites.clear()
    god()

def god():
    with open(hostpath, 'r+') as fileptr:
        content = fileptr.read()
        fileptr.seek(0)
        fileptr.truncate()
        for website in websites:
            fileptr.write(redirect+" "+website+"\n")

def options(request):
    return render(request , 'options.html')

def block_entry(request):
    blocktask = Blocks.objects.all()
    blocktext = {'Btasks':blocktask}

    return render(request , 'block_entry.html', blocktext)

def unblock_entry(request):
    unblocktask = Unblocks.objects.all()
    unblocktext = {'Utasks':unblocktask}
    return render(request , 'unblock_entry.html', unblocktext)
