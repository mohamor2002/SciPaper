from django.shortcuts import render
from django.http import HttpResponse
from .models import BasicUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from operator import itemgetter
from django.http import HttpResponseForbidden
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return HttpResponse("hello world")

@csrf_exempt    
def register(request):
    if request.method == 'POST':
        username, password ,first_name, last_name, email, gender= itemgetter('username','password', 'first_name', 'last_name', 'email', 'gender')(json.loads(request.body))
        user = authenticate(username = username, password = password)
        if user is not None:
            return HttpResponseForbidden("Email Already exists")
        else:
            user = User.objects.create_user(username = username, email = email, password = password, first_name = first_name, last_name = last_name)
            basicUser = BasicUser(user = user, gender = gender)
            basicUser.save()
            return HttpResponse("created user successefully")