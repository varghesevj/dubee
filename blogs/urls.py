from django.urls import path
from .views import blogs_list,blogs_detail

urlpatterns = [
    path('blogs/',blogs_list, name='blogs_list'),
    path('read-blog/',blogs_detail, name='blogs_detail')
]