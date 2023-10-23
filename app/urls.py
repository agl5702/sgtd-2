from django.urls import path
from . views import TorneosPendientes, DetalleTorneo, CrearTorneo, EditarTorneo, EliminarTorneo, Logueo, PaginaRegistro, Index
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', Logueo.as_view(), name='login'),
    path('registro/',PaginaRegistro.as_view(), name='registro'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('',TorneosPendientes.as_view(), name='torneos'),
    path('index/',Index,name="index"),
    path('detalle/<int:pk>', DetalleTorneo.as_view(), name='detalle'),
    path('crear-torneo/', CrearTorneo.as_view(), name='crear-torneo'),
    path('editar-torneo/<int:pk>', EditarTorneo.as_view(), name='editar-torneo'),
    path('eliminar-torneo/<int:pk>', EliminarTorneo.as_view(), name='eliminar-torneo'),
]
