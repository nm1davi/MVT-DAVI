from django.http import HttpResponse
from django.template import Template, context

def inicio(request):
    return HttpResponse("Hola soy la vista de Django")

def mi_template(request):
    
    archivo = open(r"C:\Users\USUARIO\Desktop\TrabajoMTV\templates\prueba.html", "r")
    
    template1 = Template(archivo.read())
    
    contexto1 = context()
    
    render1 = template1.render(contexto1)
    
    return HttpResponse(render1)
