from django.shortcuts import render, redirect
from .models import Beat
from .forms import BeatForm

# Create your views here.
def home(request):
	# accedemos al objeto que contiene los datos de la base
	# el método all traerá todos los vehículos que estan en la tabla, es como el  select
	beats= Beat.objects.all()
	#ahora crearemos un diccionario donde pasaremos los datos del vehículo al template

	
	#ahora se agrega para enviarlo al template y se manda la variable datos que es donde queda el diccionario
	return render(request, 'home.html',context={'datos':beats})

    
def form_beat(request):
    if request.method=='POST': 
        beat_form = BeatForm(request.POST)
        if beat_form.is_valid():
            beat_form.save()
            return redirect('home')
    else:
        beat_form= BeatForm()
    return render(request, 'core/form_beat.html', {'beat_form': beat_form})

def eliminar(request, id):
     beatEliminado = Beat.objects.get(idBeat=id)   
     beatEliminado.delete()
     return redirect ('home')

def modificar(request, id):
     beatModificado=Beat.objects.get(idBeat=id)
     datos = {
          'form' : BeatForm(instance=beatModificado)
     }
     if request.method=='POST':
          formulario = BeatForm(data=request.POST, instance=beatModificado)
          if formulario.is_valid:
               formulario.save()
               return redirect('home')
     return render(request, 'modificar.html', datos)

def ventana_inicio(request):
    # Aquí puedes agregar lógica adicional si es necesaria
    return render(request, 'ventana_inicio.html')

def ventana_info(request):
    return render(request, 'ventana_info.html')