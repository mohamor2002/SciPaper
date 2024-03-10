
from django.http import JsonResponse
from django.http import HttpResponse
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
    """
    let you register a user based on its role.

    **Context**

    ``basic user``
        An instance of :model:`authentication.BasicUser`.
    ``moderator``
        AN instance of :model:`authentication.moderator`
    ``admin``
        AN instance of :model:`authentication.admin``
        
    **request params**
        username,password,first_name,last_name,email:string
        gender: MALE OR FEMALE
        role: basic user OR admin OR moderator
    
    """
    if request.method == 'POST':
        print('here')
        fullname,password, role, email= itemgetter('fullname','password', 'role','email')(json.loads(request.body))
        user = authenticate(username = email, password = password)
        if user is not None:
            return JsonResponse({
                'message':"Email Already exists"
                }, status = 401)
        else:
            first_name = fullname.split()[0]
            if(len(fullname.split()) > 1):
                last_name = fullname.split()[1]
            else:
                last_name = " "
            user = User.objects.create_user(username = email, email = email, password = password, first_name = first_name, last_name = last_name)
            group = Group.objects.get(name = role)
            user.groups.add(group)
            if role == 'basic user':
                basic_user = BasicUser(user = user)
                basic_user.save()
            elif role == 'moderator':
                mod = moderator(user = user)
                mod.save()
            elif role == 'admin':
                adm = admin(user = user, gender = 'MALE')
                adm.save()
                djlogin(request, user)
            
            return JsonResponse({
                'message':"created user successefully",
                "user":{
                    "email":email,
                    "fullname":f'{first_name} {last_name}',
                    "favourites":[]
                }
                })
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)



def login(request):
    """
        lets you login to your existing account.
        **request params**
            username, password:string
    """
    if request.method == 'POST':
        username, password = itemgetter('username', 'password')(json.loads(request.body))
        user = authenticate(username = username, password = password)
        if user is not None :
            djlogin(request, user)
            favourites = user.basicuser.favorites.all()
            articles = []
            for i in favourites:
                articles.append(i.p_id)
            print(articles)
            return JsonResponse({
                "message":"user logged in successfully",
                "user":{
                    "email":user.email,
                    "fullname":f'{user.first_name} {user.last_name}',
                    "favourites":articles
                }
                })
        else:
            return JsonResponse({
                "message":"user not found"},status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)
        
        
          
def logout(request):
    """
        lets you end a session
    """
    if request.method == 'POST':

        djlogout(request)
        return JsonResponse({
            "message":"logout successfully",
            })
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)



@login_required
def deleteAccount(request):
    """
        lets you delete your existing account
    """
    if request.method == 'DELETE':
        user = request.user
        user.delete()
        return JsonResponse({"message":"user removed successefully"})
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)    


@login_required
@permission_required('authentication.delete_moderator',"admin",  login_url = "/")
def deleteModerator(request):
    """
        lets the admin delete an existing moderator
        **request params**
            username:string
        **context**
            ``moderator``
                An instance of :model:`authentication.moderator`
    """
    if (request.method == 'DELETE'):
          username = itemgetter('username')(json.loads(request.body))
          mod = User.objects.get(username = username)
          mod.delete()
          return JsonResponse({"message":"moderator deleted with success"})
      
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)
    
    
    
@login_required
def add_favourite(request):
    """
        lets a basic user add an article to favourites
        **context**
            ``paper``
                An instance of :model:`papers.paper`
        **request params**
            paper_id:string
    """
    if(request.method == 'POST'):
        user = request.user.basicuser
        try:
            article = paper.objects.get(p_id = json.loads(request.body)['id'])
            user.favorites.add(article)
            user.save()
            return JsonResponse({
                "message":"added paper to favorites"
            })
        except:
            return JsonResponse({
                "message":"couldnt find the paper"
            })
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)

        
def remove_favourite(request):
    """
        lets a basic user add an article to favourites
        **context**
            ``paper``
                An instance of :model:`papers.paper`
        **request params**
            paper_id:string
    """
    if(request.method == 'POST'):
        user = request.user.basicuser
        try:
            article = paper.objects.get(p_id = json.loads(request.body)['id'])
            user.favorites.remove(article)
            user.save()
            return JsonResponse({
                "message":"removed paper from favorites"
            })
        except:
            return JsonResponse({
                "message":"couldnt find the paper"
            })
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)