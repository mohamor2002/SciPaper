from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, Group
from .documents import paperDocument
from .models import paper
from custom_decorators import permission_required
import json
from elasticsearch_dsl import Search
from django.core.exceptions import ObjectDoesNotExist


@permission_required('papers.add_paper',"admin",  login_url = "/")
def create_document(request):
    if(request.method == 'POST'):
        try:
            file = next(iter(request.FILES.values()))
            document = paper(file_pdf = file)
            document.save() 
            return JsonResponse({
                'message': 'File uploaded successfully',
                'paper':document['titre', 'p_id', 'resume', 'auteurs', 'mots_cles']
                })
        except:
            return JsonResponse({'message': 'File not found'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)


@permission_required('papers.delete_paper', 'moderator', login_url='/')
def delete_document(request):
    if(request.method == 'DELETE'):
        document_id = json.loads(request.body)['id']
        try:
            document = paper.objects.get(p_id = document_id)
            document.delete()
            return JsonResponse({
                'message':f'removed the document with id ${document_id}'
            })
        except ObjectDoesNotExist:
            return JsonResponse({
                'message':'couldnt find the document'
            })
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)
    
    
@permission_required('papers.view_paper', 'basic user', login_url='/')
def get_document(request):
    if (request.method == 'GET'):
        try:
            document_id = request.GET.get("document_id")
            document = paper.objects.get(p_id = document_id)
            return JsonResponse({
                'message':'document found',
                'document':document.titre
            })
        except ObjectDoesNotExist:
            return JsonResponse({
                'message':'couldnt find the document'
            })
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)
    

@permission_required('papers.change_paper', 'moderator', login_url='/')    
def update_document(request):
    if (request.method == 'PUT'):
        req = json.loads(request.body)
        try:
            document = paper.objects.get(p_id = req['id'])
            del req['id']    
            for key, value in req.items():
                setattr(document, key, value)
            document.save(custom_save = True)
            return JsonResponse({
                'message':'updated document successfully',
                'document':'document'
            })
        except ObjectDoesNotExist:
            return JsonResponse({
                'message':'couldnt find the document'
            })
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)
    
    

def filter_documents(request):
    if(request.method == 'GET'):
        search = Search(index=paperDocument._index._name)
        for key, values in request.GET.lists():
            values = values[0].split(',')
            if len(values) > 1:
                search = search.query('terms', **{key: values})
            else:
                search = search.query('match', **{key: values[0]})

        response = search.execute().to_dict()["hits"]
        response = [i["_source"] for i in response["hits"]]
        return JsonResponse({
            "message":"papers found",
            "documents":response
        })
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)
        
        

def get_pdf(request):
    if(request.method == 'GET'):
            document_url = request.GET.get('document_url')
            with open(document_url, 'rb') as f:
                response = HttpResponse(f.read(), content_type="application/pdf")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file)
                return response
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400) 
