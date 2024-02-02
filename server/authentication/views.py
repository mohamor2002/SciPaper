
from django.http import JsonResponse
from .models import BasicUser, moderator, admin
from papers.models import paper
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login as djlogin, logout as djlogout
from operator import itemgetter
import json
from django.contrib.auth.decorators import login_required, user_passes_test
from custom_decorators import permission_required
# Create your views here.
def index(request):
    return HttpResponse("hello world")



def register(request):
    if request.method == 'POST':
        username, password ,first_name, last_name, email, gender, role = itemgetter('username','password', 'first_name', 'last_name', 'email', 'gender', 'role')(json.loads(request.body))
        user = authenticate(username = username, password = password)
        if user is not None:
            return JsonResponse({
                'message':"Email Already exists"
                }, status = 401)
        else:
            user = User.objects.create_user(username = username, email = email, password = password, first_name = first_name, last_name = last_name)
            group = Group.objects.get(name = role)
            user.groups.add(group)
            if role == 'basic user':
                basic_user = BasicUser(user = user, gender = gender)
                basic_user.save()
            elif role == 'moderator':
                mod = moderator(user = user, gender = gender)
                mod.save()
            elif role == 'admin':
                adm = admin(user = user, gender = gender)
                adm.save()
                djlogin(request, user)
            
            return JsonResponse({
                'message':"created user successefully",
                "user name":f'{user.first_name} {user.last_name}'
                })
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)



def login(request):
    if request.method == 'POST':
        username, password = itemgetter('username', 'password')(json.loads(request.body))
        user = authenticate(username = username, password = password)
        if user is not None :
            djlogin(request, user)
            return JsonResponse({
                "message":"user logged in successfully",
                "user name":f'{user.first_name} {user.last_name}'
                })
        else:
            return JsonResponse({
                "message":"user not found"},status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)
        
        
          
def logout(request):
    if request.method == 'POST':
        djlogout(request)
        return JsonResponse({
            "message":"logout successfully"
            })
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)



@login_required
def deleteAccount(request):
    if request.method == 'DELETE':
        user = request.user
        user.delete()
        return JsonResponse({"message":"user removed successefully"})
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)    


@login_required
@permission_required('authentication.delete_moderator',"admin",  login_url = "/")
def deleteModerator(request):
    if (request.method == 'DELETE'):
          username = itemgetter('username')(json.loads(request.body))
          mod = User.objects.get(username = username)
          mod.delete()
          return JsonResponse({"message":"moderator deleted with success"})
      
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)
    
    
    
@login_required
def add_favourite(request):
    if(request.method == 'POST'):
        user = request.user.user
        try:
            article = paper.objects.get(p_id = json.loads(request.body).id)
            user.favorites.add(article)
            return JsonResponse({
                "message":"added paper to favorites"
            })
        except:
            return JsonResponse({
                "message":"couldnt find the paper"
            })
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)