from django.shortcuts import render
from django.shortcuts import render,get_object_or_404, redirect
from .models import Area, Noticia
from django.utils import timezone
from .forms import AreaForm, NoticiaForm

def home(request):
	noticias = Noticia.objects.all()
	return render(request, 'portal/home.html', {'noticias':noticias})

def cadastrar_area(request):
	if request.method == "POST":
		form = AreaForm(request.POST)
		if form.is_valid():
			area = form.save(commit=False)
			area.status = True
			area.save()
			return redirect('home')
	else:
		form = AreaForm()
	return render(request, 'portal/cadastrar_area.html',{'form':form})

def listar_areas(request):
	areas = Area.objects.all()
	return render(request, 'portal/listar_areas.html',{'areas':areas})

def editar_area(request, pk):
	area = get_object_or_404(Area, pk=pk)
	if request.method == "POST":
		form = AreaForm(request.POST, instance=area)
		if form.is_valid():
			area = form.save(commit=False)
			area.save()
			return redirect('listar_areas')
	else:
		form = AreaForm(instance=area)
	return render(request, 'portal/cadastrar_area.html',{'form':form})

def desativar_area(request, pk):
	area = get_object_or_404(Area, pk=pk)
	area.desativar()
	area.save()
	return redirect('listar_areas')

def ativar_area(request, pk):
	area = get_object_or_404(Area, pk=pk)
	area.ativar()
	area.save()
	return redirect('listar_areas')

def cadastrar_noticia(request):
	if request.method == "POST":
		form = NoticiaForm(request.POST, request.FILES)
		if form.is_valid():
			noticia = form.save(commit=False)
			noticia.autor = request.user
			noticia.save()
			return redirect('home')
	else:
		form = NoticiaForm()
	return render(request, 'portal/cadastrar_noticia.html',{'form':form})
def editar_noticia(request, pk):
	noticia = get_object_or_404(Noticia, pk=pk)
	if request.method == "POST":
		form = NoticiaForm(request.POST,request.FILES, instance=noticia)
		if form.is_valid():
			noticia = form.save(commit=False)
			noticia.autor = request.user
			noticia.save()
			return redirect('home')
	else:
		form = NoticiaForm(instance=noticia)
	return render(request, 'portal/cadastrar_noticia.html',{'form':form})

def remove_noticia(request, pk):
	noticia = get_object_or_404(Noticia, pk=pk)
	noticia.delete()
	return redirect('home')

def publicar_noticia(request, pk):
	noticia = get_object_or_404(Noticia, pk=pk)
	noticia.publicar()
	return redirect('home')
def listar_noticia(request,pk):
	noticias = get_object_or_404(Noticia, pk=pk)
	return render(request, 'portal/listar_noticia.html', {'noticias':noticias})