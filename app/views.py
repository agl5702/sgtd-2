from django.shortcuts import render, redirect
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Torneo
# Create your views here.

class Logueo(LoginView):
    template_name= 'app/login.html'
    field= '__all__'
    redirect_authenticated_user= True
    #sobreescribir metodo,redireccion
    def get_success_url(self):
        return reverse_lazy('torneos')

class PaginaRegistro(FormView):
    template_name= 'app/registro.html'
    form_class= UserCreationForm
    redirect_authenticated_user= True
    success_url= reverse_lazy('torneos')
    
    
    
    def form_valid(self, form):
        usuario= form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super(PaginaRegistro,self).form_valid(form)
    
    def get(self, *args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('torneos')
        return super(PaginaRegistro, self).get(*args,**kwargs)



class TorneosPendientes(LoginRequiredMixin,ListView):#Vista de Listas
    
    model = Torneo
    context_object_name= 'torneos'

    def get_context_data(self, **kwarg):
        context=super().get_context_data(**kwarg)
        context['torneos'] = context['torneos'].filter(usuario=self.request.user)
        context['count']= context['torneos'].filter(deporte=False).count()
        #Condicion para la busqueda
        valor_buscado= self.request.GET.get('area-buscar') or ''
        if valor_buscado:
            context['torneos']= context['torneos'].filter(nombre__icontains=valor_buscado)
        context['valor_buscado']= valor_buscado

        return context



class DetalleTorneo(LoginRequiredMixin, DetailView):  # Vista de detalles
    model= Torneo
    context_object_name = 'detalles'
    template_name= 'app/torneo.html' #para personalizar el nombre de mi template
    
    def get_object(self, queryset=None):
        # Recupera el objeto Torneo
        torneo = super().get_object(queryset)

        # Verifica si el usuario actual es el propietario del torneo
        if torneo.usuario != self.request.user:
            raise Http404("No tienes permiso para ver este torneo.")

        return torneo


class CrearTorneo(LoginRequiredMixin,CreateView):  # Vsta de Crear
    model= Torneo
    fields = ['nombre', 'deporte', 'descripcion','fecha_inicio', 'fecha_final']
    success_url= reverse_lazy('torneos')
    
    def form_valid(self,form):
        form.instance.usuario= self.request.user
        return super(CrearTorneo, self).form_valid(form)

class EditarTorneo(LoginRequiredMixin,UpdateView):
    model= Torneo
    fields = ['nombre', 'deporte', 'descripcion',
    'fecha_inicio', 'fecha_final']
    success_url= reverse_lazy('torneos')
    
    def get_object(self, queryset=None):
        # Recupera el objeto Torneo
        torneo = super().get_object(queryset)

        # Verifica si el usuario actual es el propietario del torneo
        if torneo.usuario != self.request.user:
            raise Http404("No tienes permiso para editar este torneo.")

        return torneo


class EliminarTorneo(LoginRequiredMixin, DeleteView):
    model= Torneo
    fields= '__all__'
    context_object_name = 'torneos'
    success_url = reverse_lazy('torneos')

    def get_object(self, queryset=None):
        # Recupera el objeto Torneo
        torneo = super().get_object(queryset)

        # Verifica si el usuario actual es el propietario del torneo
        if torneo.usuario != self.request.user:
            raise Http404("No tienes permiso para eliminar este torneo.")

        return torneo
