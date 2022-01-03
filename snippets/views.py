#from django.http import HttpResponse, JsonResponse
#from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
#from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Snippet
from . serializers import SnippetSerializer

#@csrf_exempt
@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        #return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

    elif request.method == 'POST':
        #data = JSONParser().parse(request)
        #serializer = SnippetSerializer(data=data) 
        serializer = SnippetSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            #return JsonResponse(serializer.data, status=201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return JsonResponse(serializer.errors, status=400)   
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        #return HttpResponse(status=404)
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        #return JsonResponse(serializer.data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        #data = JSONParser().parse(request)
        #serializer = SnippetSerializer(snippet, data=data)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return JsonResponse(serializer.data)
            return Response(serializer.data)
        #return JsonResponse(serializer.errors, status=400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        #return HttpResponse(status=204)
        return Response(status=status.HTTP_204_NO_CONTENT)