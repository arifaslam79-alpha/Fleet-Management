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
    
admin.site.register(Pages, PagesAdmin)
admin.site.register(UserForm, UserFormAdmin)
admin.site.register(VehicleRegister)
admin.site.register(VehicleTrackRecord)
admin.site.register(DriverTraining)