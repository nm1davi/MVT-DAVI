from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Hola soy la vista de Django")

def mi_template(request):
    return HttpResponse("Mi template")