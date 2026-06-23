from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('alunos.urls')),
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('api/alunos', views.api_alunos, name='api_alunos'),
    path('api/alunos/<int:id>',
        views.api_alunos_detalhe,
        name='api_alunos_detalhe'),
]   