from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Tecnico
from .forms import TecnicoForm


def inicio(request):
  tecnicos = Tecnico.objects.all()
  form = TecnicoForm()
  return render(request,'inicio.html')


def registro (request):
  tecnicos = Tecnico.objects.all()
  form = TecnicoForm()
  return render(request, 'registro.html', {'tecnicos' : tecnicos, 'form' : form})

#def consulta (request):
    #return HttpResponse("Hoja de consulta")
    

# Create your views here.
