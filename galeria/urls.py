from django.urls import path
from galeria.views import index, catalogo

urlpatterns = [ 
    path('', index, name='index'),
    path('formulario/', catalogo, name= 'catalogo')
]