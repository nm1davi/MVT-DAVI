from .views import inicio, listado_familia, mi_template
from django.urls import path
urlpatterns = [
    path('', inicio),
    path('mi-template/', mi_template),
    path('listado-familia', listado_familia),


]
