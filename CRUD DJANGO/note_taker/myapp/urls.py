from django.contrib import admin
from django.urls import  path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('addnote',views.addnote,name='addnote'),
    path('del/<int:id>',views.delete,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('contactus',views.contactus,name='contactus'),
    path('contactorg',views.contactorg,name='contact'),
]

