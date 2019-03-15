from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')
