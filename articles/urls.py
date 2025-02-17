from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [
    path('create/', views.article_create, name='create'),
    path('detail/<int:post_id>/', views.article_detail, name='detail'),
    path('category/<str:category>/', views.post_by_category, name='category'),
]