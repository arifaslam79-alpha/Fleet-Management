from django.shortcuts import render
from django.http import JsonResponse
from .models import Pages, UserForm,VehicleRegister,VehicleTrackRecord,DriverTraining
from django.db.models import Count  
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib.auth.models import User  
import matplotlib.pyplot as plt  
import matplotlib
matplotlib.use('agg')
from io import BytesIO  
import base64  
import random  
import string 
import datetime 
from django.db.models.functions import TruncDate  

# Create your views here.
def home(request):
    try:
        home_obj = Pages.objects.get(name='home', status='1');
    except Pages.DoesNotExist:
        home_obj = []
    context = {
        'data': home_obj
    }
    return render(request,"fleets_management/index.html",context);
    
def about(request):
    try:
        about_obj = Pages.objects.get(name='about', status='1');
    except Pages.DoesNotExist:
        about_obj = []
    context = {
        'data': about_obj
    }
    return render(request,"fleets_management/about.html",context);

def contact(request):
    try:
        contact_obj = Pages.objects.get(name='contact', status='1');
    except Pages.DoesNotExist:
        contact_obj = []
    context = {
        'data': contact_obj
    }
    return render(request,"fleets_management/contact.html",context);

def driver_training(request):
    try:
        driver_training_obj = VehicleRegister.objects.all()
        driver_training_pobj = Pages.objects.get(name='driver-training', status='1');
        
        driver_training_plot = DriverTraining.objects.values('driver_training_status').annotate(count=Count('vehicle')).order_by('count')[:5]
        
        DriverTraingStatus = []
        NoOfVehicle = []
        for item in driver_training_plot:
            DriverTraingStatus.append('Present' if item['driver_training_status']=='Y' else 'Absent')
            NoOfVehicle.append(item['count'])
        
        plt.plot(DriverTraingStatus, NoOfVehicle)  
        plt.title('X=Training Availability, Y=No. of drivers')
        buffer = BytesIO()  
        plt.savefig(buffer, format='png')  
        buffer.seek(0)  
        plot_url = base64.b64encode(buffer.read()).decode('utf-8')  
        plt.close()

    except VehicleRegister.DoesNotExist:
        driver_training_pobj = []
        plot_url = ''
    context = {
        'data': driver_training_pobj,
        'plot_url': plot_url
    }
    return render(request,"fleets_management/driver_training.html",context)

def vehicle_track(request):
    try:
        vehicletrack_obj = Pages.objects.get(name='vehicle-tracking', status='1');

        vehicletrack_by_date = VehicleTrackRecord.objects.values('vehicle','vehicle_condition').order_by('vehicle_condition')[:5]
        
        vehicleCond = []
        vehicleName = []
        for item in vehicletrack_by_date: 
            vehicleReg = VehicleRegister.objects.get(pk=item['vehicle'])
            vehicleName.append(vehicleReg.vehicle_name)
            vehicleCond.append(item['vehicle_condition'])
       
        plt.plot(vehicleName, vehicleCond)  
        plt.title('X=Vehicle Name, \nY=Vehicle Condition(0=Bad | 1=Below Average | 2=Average | 3=Good)')
        buffer = BytesIO()  
        plt.savefig(buffer, format='png')  
        buffer.seek(0)  
        plot_url = base64.b64encode(buffer.read()).decode('utf-8')  
        plt.close()

    except VehicleRegister.DoesNotExist:
        vehicletrack_obj=[]
        plot_url =''
    context = {
        'data': vehicletrack_obj,
        'plot_url': plot_url
    }
    return render(request,"fleets_management/vehicle_track.html",context)

def vehicle_reg(request):
    try:
        vehiclereg_obj = Pages.objects.get(name='vehicle-registration', status='1')

        vehicle_by_date = VehicleRegister.objects.annotate(date=TruncDate('vehicle_reg_date')).values('date').annotate(count=Count('id')).order_by('date')[:5]
        registered_date = []
        registered_count = []
        for item in vehicle_by_date:  
            registered_date.append(str(item['date']))
            registered_count.append(item['count'])
        plt.plot(registered_date, registered_count)  
        plt.title('X=Registration Date, Y=No. of Registrations')
        buffer = BytesIO()  
        plt.savefig(buffer, format='png')  
        buffer.seek(0)  
        plot_url = base64.b64encode(buffer.read()).decode('utf-8')  
        plt.close()

    except VehicleRegister.DoesNotExist:
        plot_url = '';
        vehiclereg_obj=[]
    context = {
        'data': vehiclereg_obj,
        'plot_url': plot_url
    }
    return render(request,"fleets_management/vehicle_reg.html",context);

def contact_form(request):
    if request.method == 'POST':
        formObj = UserForm.objects.all().last()
        id=1
        if formObj.id:
            id = formObj.id+1
            
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        form = UserForm(id,name,email,phone,message)
        if form:
            form.save()
            msg = "<html><head><title>Contact Form</title></head><body>"
            msg += "<p>Hi "+name+", <br>Thank you for contacting us with your valulable comments and details mentioned below, we will contact you if it is required.</p>"
            msg +="<p><strong>Name: </strong>"+name+"</p>"
            msg +="<p><strong>Email Address: </strong>"+email+"</p>"
            msg +="<p><strong>Phone No.: </strong>"+phone+"</p>"
            msg +="<p><strong>Comments: </strong>"+message+"</p>"
            msg +="<p>Please let us know for any further assistance.</p>"
            msg +="<p>Thanks & Regards</p>"
            msg += "<p>Support team</p>"
            msg += "</body></html>"
            send_mail(
                'Fleet Management - Contact form submission',
                msg,
                "noreply@gmail.com",
                ['arifaslam79@gmail.com',email],
                fail_silently=False,
                html_message=msg
            )
            return JsonResponse({'message': 'Form submitted successfully.'})  
        else:  
            return JsonResponse({'errors': form.errors}, status=400)  
    return JsonResponse({'error': 'Invalid request'}, status=400)  

