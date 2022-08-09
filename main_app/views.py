from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Hospital
from .forms import DeviceForm

class HospitalCreate(CreateView):
  model = Hospital
  fields = '__all__'

class HospitalUpdate(UpdateView):
  model = Hospital
  fields = '__all__'

class HospitalDelete(DeleteView):
  model = Hospital
  success_url = '/hospitals/'


def home(request):
  return render(request, 'home.html')
def hospitals(request):
  hospitals = Hospital.objects.all()
  return render(request, 'hospitals/index.html', { 'hospitals': hospitals })
def hospitals_detail(request, hospital_id):
  hospital = Hospital.objects.get(id=hospital_id)
  device_form = DeviceForm()
  return render(request, 'hospitals/detail.html', { 'hospital': hospital, 'device_form': device_form })
def add_device(request, hospital_id):
  form = DeviceForm(request.POST)
  if form.is_valid():
    new_device = form.save(commit=False)
    new_device.hospital_id = hospital_id
    new_device.save()
  return redirect('hospitals_detail', hospital_id=hospital_id)
def hospitals_create(request, hospital_id):
  hospital = Hospital.objects.get(id=hospital_id)
  return render(request, 'hospitals/detail.html', { 'hospital': hospital })
