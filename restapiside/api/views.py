from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view #function based views

from rest_framework.views import APIView #class views

from rest_framework.generics import get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin, DestroyModelMixin, UpdateModelMixin, RetrieveModelMixin

from rest_framework import generics

from restapiside.models import Article, Author
from restapiside.api.serializers import ArticleSerializer, AuthorSerializer

# CONCRETE VIEWS EXAMPLE -----------------------------------------------------------------------------------------------
class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorIdListUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class ArticleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleIdListUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

# GENERIC API VIEWS EXAMPLE --------------------------------------------------------------------------------------------
# class AuthorListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#CLASS BASED API VIEW EXAMPLE ------------------------------------------------------------------------------------------
# class AuthorListCreateAPIView(APIView):
#     def get(self,request):
#         # articles = Article.objects.filter(activity_status=True)
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many=True, context={'request':request})
#         return Response(serializer.data)
#     def post(self,request):
#         serializer = AuthorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class AuthorIdListUpdateDeleteAPIView(APIView):
#     def get_object(self, pk):
#         author = get_object_or_404(Article,pk=pk)
#         return author
#     def get(self, request, pk):
#         author = self.get_object(pk=pk)
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data)
#     def put(self, request, pk):
#         author = self.get_object(pk=pk)
#         serializer = AuthorSerializer(author, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, pk):
#         article = self.get_object(pk=pk)
#         article.delete()
#         return Response(
#             {
#                 'process': {
#                     'code': 204,
#                     'message': f'Successfuly deleting for this id {pk}'
#                 }
#             },
#             status=status.HTTP_204_NO_CONTENT
#         )

# class ArticleListCreateAPIView(APIView):
#     def get(self,request):
#         # articles = Article.objects.filter(activity_status=True)
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class ArticleIdListUpdateDeleteAPIView(APIView):
#     def get_object(self, pk):
#         article = get_object_or_404(Article,pk=pk)
#         return article
#     def get(self, request, pk):
#         article = self.get_object(pk=pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#     def put(self, request, pk):
#         article = self.get_object(pk=pk)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, pk):
#         article = self.get_object(pk=pk)
#         article.delete()
#         return Response(
#             {
#                 'process': {
#                     'code': 204,
#                     'message': f'Successfuly deleting for this id {pk}'
#                 }
#             },
#             status=status.HTTP_204_NO_CONTENT
#         )

# FUNCTION BASED API VIEWS EXAMPLE -------------------------------------------------------------------------------------
# @api_view(['GET', 'POST']) #function based
# def article_list_create_api_view(request):
#
#     if request.method == 'GET':
#         articles = Article.objects.filter(activity_status=True)
#         # articles = Article.objects.all()
#         serializer = ArticleSerializer(articles,many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE']) #function based
# def article_id_list_update_delete_api_view(request,pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return Response(
#             {
#                 'errors':{
#                     'code':404,
#                     'message':f'No article found with this number -> {pk}'
#                 }
#             },
#             status=status.HTTP_404_NOT_FOUND
#         )
#
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(
#             {
#                 'process': {
#                     'code': 204,
#                     'message': f'Successfuly deleting for this id {pk}'
#                 }
#             },
#             status=status.HTTP_204_NO_CONTENT
#         )