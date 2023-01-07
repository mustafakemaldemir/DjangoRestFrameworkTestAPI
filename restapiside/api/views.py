from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view #function based views

from restapiside.models import Article
from restapiside.api.serializers import ArticleSerializer

#FUNCTION BASED API VIEWS EXAMPLE
@api_view(['GET', 'POST']) #function based
def article_list_create_api_view(request):

    if request.method == 'GET':
        makaleler = Article.objects.filter(activity_status=True)
        # makaleler = Makale.objects.all()
        serializer = ArticleSerializer(makaleler,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE']) #function based
def article_id_list_update_delete_api_view(request,pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(
            {
                'errors':{
                    'code':404,
                    'message':f'No article found with this number -> {pk}'
                }
            },
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article.delete()
        return Response(
            {
                'process': {
                    'code': 204,
                    'message': f'Successfuly deleting for this id {pk}'
                }
            },
            status=status.HTTP_204_NO_CONTENT
        )
