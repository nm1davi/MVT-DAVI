from django.http import HttpResponse
from django.template import Template, Context, loader

def inicio(request):
    return HttpResponse("Hola soy la vista de Django")

def mi_template(request):
    
    # archivo = open(r"C:\Users\USUARIO\Desktop\TrabajoMTV\templates\prueba.html", "r")
    
    template1 = loader.get_template("prueba.html")
    
    nombre = "Momia"
    # template1 = Template(archivo.read())
    # contexto1 = Context()
    apellido = "Blanca"
    render1 = template1.render({"nombre" : nombre, "apellido" : apellido})
    
    return HttpResponse (render1)
