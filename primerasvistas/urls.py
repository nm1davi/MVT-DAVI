from .views import inicio, mi_template, listado_familia
from django.urls import path
urlpatterns = [
    path('', inicio),
    path('mi-template/', mi_template),
    path('lista-familia/', listado_familia),

]
