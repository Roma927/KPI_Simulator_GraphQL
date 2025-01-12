# from django.db import models

# class Simulator(models.Model):
#     INTERVAL_CHOICES = [
#         ('hourly', 'Hourly'),
#         ('daily', 'Daily'),
#         ('weekly', 'Weekly'),
#     ]
    
#     start_date = models.DateTimeField()
#     interval = models.CharField(max_length=10, choices=INTERVAL_CHOICES)
#     kpi_id = models.IntegerField()

from django.db import models
from datetime import timedelta

class Simulator(models.Model):
    kpi_id = models.IntegerField()  # Assuming `kpi_id` is an integer
    start_date = models.DateTimeField()  # The start date for the simulator
    interval = models.CharField(max_length=255)  # Cron expression or timedelta format

    def __str__(self):
        return f"Simulator {self.id} for KPI {self.kpi_id}"
