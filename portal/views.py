from django.shortcuts import render
from django.shortcuts import render,get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm

def home(request):
	return render(request, 'portal/home.html', {})
