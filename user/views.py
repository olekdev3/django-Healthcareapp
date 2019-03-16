from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from user.models import Patient, Details
# Create your views here.


@login_required
def dashboard(request):
    return render(request, 'user/dashboard.html')


def newPatient(request):
    return render(request, 'user/newPatient.html')


def about(request):
    return render(request, 'user/about.html')


@login_required
def profile(request):
    return render(request, 'user/profile.html')


class DoctorsList(ListView):
    model = Details
    template_name = 'user/doctors.html'
    context_object_name = 'details'


class PatientList(ListView):
    model = Patient
    template_name = 'user/patients.html'
    context_object_name = 'patients'


class HistoryList(ListView):
    model = Details
    template_name = 'user/history.html'
    context_object_name = 'details'
    context = {'patients': Patient}


def report(request):
    patients=Patient.objects.all().values()
    details=Details.objects.all().values()
    return render(request,'user/report.html',{'patients': patients,'details': details})
