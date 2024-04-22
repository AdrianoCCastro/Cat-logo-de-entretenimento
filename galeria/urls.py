from django.urls import path
from galeria.views import index, formulario

urlpatterns = [ 
    path('', index, name='index'),
    path('formulario/', formulario, name= 'formulario')
]