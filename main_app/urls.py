from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('hospitals/', views.hospitals, name='hospitals'),
  path('hospitals/<int:hospital_id>/', views.hospitals_detail, name='hospitals_detail'),
  path('hospitals/create/', views.HospitalCreate.as_view(), name='hospitals_create'),
  path('hospitals/<int:pk>/update/', views.HospitalUpdate.as_view(), name='hospitals_update'),
  path('hospitals/<int:pk>/delete/', views.HospitalDelete.as_view(), name='hospitals_delete'),
  path('hospitals/<int:hospital_id>/add_device/', views.add_device, name='add_device'),
]

