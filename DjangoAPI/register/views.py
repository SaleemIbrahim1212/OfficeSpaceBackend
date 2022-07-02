from pydoc import resolve
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.

def register( response):
    if (response.method == "POST"):
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})





def getuser(response):
    
    user = authenticate(username=response.GET.get('username'), password=response.GET.get('password') )
    if user is not None:

        data = {
           'isauth' : '1',
           'username' : response.GET.get('username')
        }
        return JsonResponse(data)
    else:
        data = {
            'isauth': '0',
            'username': 'N/A'
        }
        return JsonResponse(data)

    
