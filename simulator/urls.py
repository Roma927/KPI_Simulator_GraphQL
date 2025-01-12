from django.urls import path
from .views import KpiCalculator

urlpatterns = [
    path('calculate/', KpiCalculator.as_view(), name='calculate_kpi'),
]