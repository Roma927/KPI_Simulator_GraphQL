from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class KpiCalculator(APIView):
    def post(self, request):
        value = request.data.get('value')
        kpi_id = request.data.get('kpi_id')
        result = self.calculate_kpi(value, kpi_id)
        return Response({'result': result})
    
    def calculate_kpi(self, value, kpi_id):
        calculations = {
            1: lambda x: x * 1.5,
            2: lambda x: x * 0.8,
            3: lambda x: x ** 2,
        }
        return calculations.get(kpi_id, lambda x: x)(float(value))