from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import FormReserva
from .models import Reserva
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.


def registro(request):
    if request.method == "GET":
        return render(request, "registro_form.html", {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            # registro de ususario
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                return redirect("reserva")
            except IntegrityError:
                return render(
                    request,
                    "registro_form.html",
                    {"form": UserCreationForm, "error": "El usuario ya existe"},
                )

        return render(
            request,
            "registro_form.html",
            {"form": UserCreationForm, "error": "Los password no coinciden."},
        )


def home(request):
    return render(request, 'home.html')



@login_required
def reserva(request):
     reservas = Reserva.objects.filter(user = request.user, realizado__isnull = True)
    
     return render(request, "reservas.html",{
        'reservas' : reservas
    })

@login_required
def crear_res(request):
    
    if request.method =='GET':
         return render(request , 'crear_reserva.html', {
        'form': FormReserva
    })
    else:
        try:
            form = FormReserva(request.POST)
            nueva_reserva = form.save(commit=False)
            nueva_reserva.user = request.user
            nueva_reserva.save()
        
            return redirect('reserva')
        except:
            return render(request , 'crear_reserva.html', {
            'form': FormReserva,
            'error': 'Por favor ingrese datos validos'
            })
    
    
   
@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect("home")


def inicio_sesion(request):
    if request.method == "GET":
        return render(request, "login.html", {"form": AuthenticationForm})
    else:
        
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
          return render(request, "login.html", {"form": AuthenticationForm, 'error':'Usuario o password incorrecto'})
        else:
            login(request,user)
            return redirect('reserva')
        
        
@login_required          
def eventos_detalles(request, res_id):
    if request.method == 'GET':
        reserva =  get_object_or_404(Reserva, pk=res_id, user = request.user)
        form = FormReserva(instance=reserva)
        return render(request, 'detalles_eventos.html',{
            'reserva': reserva,
            'form' : form
            
        })
    else:
       try:
            reserva =  get_object_or_404(Reserva, pk= res_id, user= request.user)
            form = FormReserva(request.POST, instance=reserva)
            form.save()
            return redirect('reserva')
       except ValueError: 
           return render(request, 'detalles_eventos.html',{
               'error': 'Error actualizando reserva'
           })
           
   
   
   
@login_required
def evento_realizado(request, res_id):
    reserva = get_object_or_404(Reserva, pk=res_id, user=request.user)

    if request.method == 'POST':
        reserva.realizado = timezone.now()
        reserva.save()
        return redirect('reserva')
   
    
    
        
            

@login_required
def eliminar(request, res_id):
    reserva = get_object_or_404(Reserva, pk=res_id, user= request.user)
    if request.method == 'POST':
        reserva.delete()
        return redirect('reserva')
    
@login_required
def eventos_completados(request):
     reservas = Reserva.objects.filter(user = request.user, realizado__isnull = False).order_by('-realizado')
    
     return render(request, "reservas.html",{
        'reservas' : reservas
    })
 
        
        
   

        
        
