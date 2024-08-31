from django.urls import path
from . import views
urlpatterns=[
    path('index/',views.index,name='index'),
    path('',views.create,name='create'),
    path('view/',views.view,name='view'),
    path('delete/<pk>',views.delete,name='delete'),
    path('edit/<pk>',views.edit,name='edit')
]