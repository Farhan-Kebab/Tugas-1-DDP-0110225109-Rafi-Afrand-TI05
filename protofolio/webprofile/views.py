from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'aboutme.html')

def contact(request):
    return render(request, 'gallery.html')

def login(request):
    return render(request, 'index.html')