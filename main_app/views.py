from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Hospital
from .forms import DeviceForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


class HospitalCreate(LoginRequiredMixin, CreateView):
  model = Hospital
  fields = '__all__'
  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class HospitalUpdate(LoginRequiredMixin, UpdateView):
  model = Hospital
  fields = '__all__'

class HospitalDelete(LoginRequiredMixin, DeleteView):
  model = Hospital
  success_url = '/hospitals/'

class Home(LoginView):
  template_name = 'home.html'

@login_required 
def hospitals(request):
  hospitals = Hospital.objects.filter(user=request.user)
  return render(request, 'hospitals/index.html', { 'hospitals': hospitals })

@login_required 
def hospitals_detail(request, hospital_id):
  hospital = Hospital.objects.get(id=hospital_id)
  device_form = DeviceForm()
  return render(request, 'hospitals/detail.html', { 'hospital': hospital, 'device_form': device_form })

@login_required 
def add_device(request, hospital_id):
  form = DeviceForm(request.POST)
  if form.is_valid():
    new_device = form.save(commit=False)
    new_device.hospital_id = hospital_id
    new_device.save()
  return redirect('hospitals_detail', hospital_id=hospital_id)

@login_required 
def hospitals_create(request, hospital_id):
  hospital = Hospital.objects.get(id=hospital_id)
  return render(request, 'hospitals/detail.html', { 'hospital': hospital })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('hospitals')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
