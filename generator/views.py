import string

from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    length = 10

    thepassword = ''
    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, 'password.html', {'password': thepassword})
