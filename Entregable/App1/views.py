from django.shortcuts import render
from App1.models import Familia
from django.http import HttpResponse

# Create your views here.

def mostrar_familia(request):
    f1 = Familia(nombre = 'Jennifer', apellido = 'Perdigon',edad = 38, fecha_nacimiento = '1984-07-19', email = 'jennifer721@gmail.com')
    f2 = Familia(nombre = 'Rosa', apellido = 'Lorenzo',edad = 65, fecha_nacimiento = '1957-09-05', email = 'rlorenzo@gmail.com')
    f3 = Familia(nombre = 'Miguel', apellido = 'Perdigon',edad = 70, fecha_nacimiento = '1952-02-16', email = 'miguelpc@gmail.com')
    f4 = Familia(nombre = 'Ricardo', apellido = 'Perdigon',edad = 42, fecha_nacimiento = '1980-01-25', email = 'viturino@gmail.com')

    return render(request, 'familia.html',{'familia':[f1,f2,f3,f4]})