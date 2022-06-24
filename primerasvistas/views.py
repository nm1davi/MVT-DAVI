from re import template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader

from primerasvistas.models import Familiar

def inicio(request):
    return HttpResponse("Hola soy la vista de Django")

def mi_template(request):
    
    
    template1 = loader.get_template("prueba.html")
    
    Integrante = Familiar(nombre="Tomas", edad="21", fecha_nacimiento = "2001-07-09")
    
    Integrante.save()
    
    render1 = template1.render({"Integrante": Integrante,})
    
    return HttpResponse (render1)


def listado_familia(request):
    
    template = loader.get_template("listado_familia.html")
    
    lista_familia = Familiar.objects.all()
    
    render = template.render({"lista": lista_familia})

    return HttpResponse(render)

