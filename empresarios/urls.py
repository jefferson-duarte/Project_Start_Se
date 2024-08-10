from django.urls import path

from . import views

app_name = 'empresarios'

urlpatterns = [
    path('cadastrar_empresa/', views.cadastrar_empresa, name='cadastrar_empresa'),  # noqa:E501
    path('listar_empresas/', views.listar_empresas, name='listar_empresas'),
    path('empresa/<int:id>/', views.empresa, name='empresa'),
]
