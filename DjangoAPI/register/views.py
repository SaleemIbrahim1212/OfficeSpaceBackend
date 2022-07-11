from logging import exception
from pydoc import resolve
from sqlite3 import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import BookingSpace
from django.core import serializers
from .serializers import BookingSerializers

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
           'username' : response.GET.get('username'),
           'email' : response.user.email,
        }
        return JsonResponse(data)
    else:
        data = {
            'isauth': '0',
            'username': 'N/A',
            'email': 'N/A'
        }
        return JsonResponse(data)



def createBookingSpace(response):
    if response.method == "GET":
        space = BookingSpace(username= response.GET.get('username'), email = response.GET.get('email'), room = response.GET.get('room'), time = response.GET.get('time'), date = response.GET.get('date'))
        try:
         space.save()
         response = { 'issaved' : 'True'}
         return JsonResponse( response)

        except:
            response = {'issaved': 'False'}
            return JsonResponse(response)


def getUserBookingSpace(response):
    if response.method == "GET":
        info = BookingSpace.objects.filter(username = response.GET.get('username'))
        list = BookingSerializers(info, many=True)
        return JsonResponse(list.data, safe=False)





