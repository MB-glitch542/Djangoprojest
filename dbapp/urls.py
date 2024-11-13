from  django.urls import path
from . import views



urlpatterns=[

    path('',views.blog_list,name='blog_list'),
    path('<int:post_id>',views.blog_details,name='blog_details'),


]