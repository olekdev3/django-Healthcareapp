from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
def dashboard(request):
    return render(request,'user/dashboard.html')

def newPatient(request):
    return render(request, 'user/newPatient.html')
    
