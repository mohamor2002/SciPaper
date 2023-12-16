from django.shortcuts import render
from django.http import HttpResponse
from .models import BasicUser
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login as djlogin, logout as djlogout
from operator import itemgetter
from django.http import HttpResponseForbidden, HttpResponseNotFound
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return HttpResponse("hello world")

@csrf_exempt    
def register(request):
    group = Group.objects.get(name = 'basic user')
    if request.method == 'POST':
        username, password ,first_name, last_name, email, gender= itemgetter('username','password', 'first_name', 'last_name', 'email', 'gender')(json.loads(request.body))
        user = authenticate(username = username, password = password)
        if user is not None:
            return HttpResponseForbidden("Email Already exists")
        else:
            user = User.objects.create_user(username = username, email = email, password = password, first_name = first_name, last_name = last_name)
            user.groups.add(group)
            basicUser = BasicUser(user = user, gender = gender)
            basicUser.save()
            return HttpResponse("created user successefully")


# @csrf_exempt
def login(request):
    if request.method == 'POST':
        username, password = itemgetter('username', 'password')(json.loads(request.body))
        user = authenticate(username = username, password = password)
        if user is not None :
            djlogin(request, user)
            return HttpResponse("user logged in successfully")
        else:
            return HttpResponseNotFound("user not found")
        
        
# @csrf_exempt    
def logout(request):
    if request.method == 'POST':
        djlogout(request)
        return HttpResponse("logout successfully")


@login_required
def deleteAccount(request):
    if request.method == 'DELETE':
        user = request.user
        user.delete()
        return HttpResponse("user removed successefully")