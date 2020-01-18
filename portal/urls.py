from django.urls import path
from . import views

urlpatterns=[
	path('', views.home, name='home'),
	path('noticias/nova_area', views.cadastrar_area, name='cadastrar_area'),
	path('noticias/lista_areas', views.listar_areas, name='listar_areas'),
	path('noticias/<int:pk>/edita_area', views.editar_area, name='editar_area'),
	path('noticias/<int:pk>/desativa_area', views.desativar_area, name='desativar_area'),
	path('noticias/<int:pk>/ativa_area', views.ativar_area, name='ativar_area'),

	path('noticias/nova_noticia', views.cadastrar_noticia, name='cadastrar_noticia'),
	path('noticias/<int:pk>/edita_noticia', views.editar_noticia, name='editar_noticia'),
	path('noticias/<int:pk>/remove', views.remove_noticia, name='remove_noticia'),
	path('noticias/<int:pk>/publica_noticia', views.publicar_noticia, name='publicar_noticia'),
	path('noticias/<int:pk>/lista_noticia', views.listar_noticia, name='listar_noticia'),
]