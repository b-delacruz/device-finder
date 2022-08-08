from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Hospital

class HospitalCreate(CreateView):
  model = Hospital
  fields = '__all__'
  success_url: '/hospitals/'

def login(request):
  return HttpResponse('<h1>Hello World</h1>')
def home(request):
  return render(request, 'home.html')
def hospitals(request):
  hospitals = Hospital.objects.all()
  return render(request, 'hospitals/index.html', { 'hospitals': hospitals })
def hospitals_detail(request, hospital_id):
  hospital = Hospital.objects.get(id=hospital_id)
  return render(request, 'hospitals/detail.html', { 'hospital': hospital })
def hospitals_create(request, hospital_id):
  hospital = Hospital.objects.get(id=hospital_id)
  return render(request, 'hospitals/detail.html', { 'hospital': hospital })