from django.contrib import admin
from .models import Pages, UserForm,VehicleRegister,VehicleTrackRecord,DriverTraining
from django_summernote.widgets import SummernoteWidget 
from django.db import models 

# Register your models here.
class PagesAdmin(admin.ModelAdmin): 
     formfield_overrides = { 
            models.TextField: {'widget': SummernoteWidget}, 
     }
class UserFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')

class VehicleRegisterAdmin(admin.ModelAdmin):
    list_display = ('vehicle_number', 'vehicle_name', 'vehicle_model', 'vehicle_owner_phone', 'vehicle_owner_email', 'vehicle_reg_date')

class VehicleTrackRecordAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'vehicle_condition')

class DriverTrainingAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'driver_name', 'driver_phone', 'driver_email', 'is_training_needed', 'training_name', 'training_date', 'driver_training_status')

admin.site.register(Pages, PagesAdmin)
admin.site.register(UserForm, UserFormAdmin)
admin.site.register(VehicleRegister, VehicleRegisterAdmin)
admin.site.register(VehicleTrackRecord, VehicleTrackRecordAdmin)
admin.site.register(DriverTraining, DriverTrainingAdmin)