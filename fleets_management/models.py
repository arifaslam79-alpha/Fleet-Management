from django.db import models
from datetime import datetime  

# Create your models here.
class Pages(models.Model):
     name = models.CharField(max_length=200)
     description = models.TextField()
     iframe_code = models.CharField(max_length=1000, default='')
     status = models.CharField(max_length=200, choices=[('1', 'Enable'),('0', 'Disable')], default='1')
     def __str__(self):
         return self.name
         
         
class UserForm(models.Model):
    name  = models.CharField(max_length=100)  
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)    
    message = models.TextField()
    def __str__(self):
        return self.name
        
class VehicleRegister(models.Model):
    vehicle_name  = models.CharField(max_length=100)  
    vehicle_model = models.CharField(max_length=100)
    vehicle_number = models.CharField(max_length=100)    
    vehicle_owner_phone = models.CharField(max_length=15)
    vehicle_owner_email = models.CharField(max_length=100)
    vehicle_reg_date = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.vehicle_number
        
class VehicleTrackRecord(models.Model):
    vehicle  = models.ForeignKey(VehicleRegister, on_delete=models.CASCADE)
    is_email_sent = models.CharField(max_length=2)
    email_date = models.DateField(default=datetime.now)
    vehicle_condition = models.CharField(max_length=100, choices=[('3', 'Good'),('2', 'Average'),('1', 'Below Average'), ('0', 'Bad')])
    def __str__(self):
        return self.vehicle.vehicle_number
        
class DriverTraining(models.Model):
    vehicle  = models.ForeignKey(VehicleRegister, on_delete=models.CASCADE)
    driver_name = models.CharField(max_length=100)
    driver_phone = models.CharField(max_length=100)   
    driver_email = models.CharField(max_length=100)
    is_training_needed = models.CharField(max_length=2)
    training_name = models.CharField(max_length=100)
    training_date = models.DateField()
    driver_training_status = models.CharField(max_length=2)
    def __str__(self):
        return self.vehicle.vehicle_number