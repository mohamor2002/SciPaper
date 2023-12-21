from django.http import HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
def index(request):

    headers = {
        'Content-Type': 'application/binary',
    }

    with open('server/baseApp/shi2014.pdf', 'rb') as f:
        data = f.read()

    response = requests.post('http://cermine.ceon.pl/extract.do', headers=headers, data=data)
    return HttpResponse(response)

    
def test(user):
    return user.has_perm('authentication.delete_moderator')

@csrf_exempt
@user_passes_test(test)
def deleteModerator(request):
    if (request.method == 'DELETE'):
        content_type = ContentType.objects.get(app_label='authentication', model='moderator')

# Retrieve default permissions for the content type
        default_permissions = Permission.objects.filter(content_type=content_type)

# Print default permission names
        for perm in default_permissions:
            print(perm.codename)
        # username = itemgetter('username')(json.loads(request.body))
        # mod = User.objects.get(username = username)
        # mod.delete()
        return HttpResponse("moderator deleted with success")