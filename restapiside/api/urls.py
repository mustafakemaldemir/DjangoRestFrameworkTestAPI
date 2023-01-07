from django.urls import path
from restapiside.api import views as api_views

urlpatterns = [
    path('article/',api_views.article_list_create_api_view, name='article-list-create'),
    path('article/<int:pk>',api_views.article_id_list_update_delete_api_view, name='article-update-delete'),
]