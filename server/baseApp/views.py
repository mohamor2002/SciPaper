from django.http import HttpResponse
import requests

def index(request):

    headers = {
        'Content-Type': 'application/binary',
    }

    with open('server/baseApp/shi2014.pdf', 'rb') as f:
        data = f.read()

    response = requests.post('http://cermine.ceon.pl/extract.do', headers=headers, data=data)
    return HttpResponse(response)