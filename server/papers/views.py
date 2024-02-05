from django.http import HttpResponse, JsonResponse,FileResponse
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
    
    
# @permission_required('papers.view_paper', 'basic user', login_url='/')
def get_documents(request):
    if (request.method == 'GET'):
        try:
            ids = request.GET.getlist('id[]')
            print(ids)
            articles = []
            for i in ids:
                search = Search(index=paperDocument._index._name)
                search = search.query('match', **{'id': i})
                response = search.execute().to_dict()["hits"]
                response = [i["_source"] for i in response["hits"]]
                articles.append(response[0])
            return JsonResponse({
                'message':'document found',
                'documents':articles
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
            key = key.rstrip('[]')
            print(key)
            print(values)
            if len(values) > 1:
                search = search.query('terms', **{key:values})
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
        
        

def get_pdf(request, id):
    if(request.method == 'GET'):
            # document_url = request.GET.get('document_url')
            papier = paper.objects.get(p_id = id)
            document_url = papier.file_pdf.path
            with open(document_url, 'rb') as f:
                # response = HttpResponse(f.read(), content_type="application/pdf")
                response = HttpResponse(f.read(), content_type='application/pdf')
                response["Content-Disposition"] = "attachment; filename=file.pdf"
                return response
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400) 



def get_text(request, id):
    if(request.method == 'GET'):
            papier = paper.objects.get(p_id = id)
            text = papier.texte_integral
                # response = HttpResponse(f.read(), content_type="application/pdf")
            response = HttpResponse(content_type='text/plain')
            response["Content-Disposition"] = "attachment; filename=file.txt"
            response.write(text)
            return response
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400) 