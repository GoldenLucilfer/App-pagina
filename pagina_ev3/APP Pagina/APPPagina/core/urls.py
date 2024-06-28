from django.urls import path
from .views import home, form_beat, eliminar, modificar, ventana_inicio, ventana_info

urlpatterns = [
    path('', ventana_inicio, name='home'),        # Ruta raíz para ventana_inicio
    path('form_beat/', form_beat, name='form_beat'),
    path('home/', home, name='tracklist'),        # Ruta para la antigua home
    path('eliminar/<int:id>/', eliminar, name='eliminar'),
    path('modificar/<int:id>/', modificar, name='modificar'),
    path('ventana_info/', ventana_info, name='ventana_info')
    ]
