from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm
# Create your views here.
def index(request):
    return render(request,'index.html')
def about_us(request):
    return render(request,'about_us.html')
def courses(request):
    return render(request,'courses.html')
def blog(request):
    return render(request,'blog.html')
def shop(request):
    products = product.objects.all()
    context = {'products': products}
    return render(request, 'shop.html', context)
def accounting(request):
    return render(request,'accounting.html')
def cttc(request):
    return render(request,'cttc.html')
def data_entry(request):
    return render(request,'data_entry.html')
def dca(request):
    return render(request,'dca.html')
def graphic(request):
    return render(request,'graphic.html')
def netfix(request):
    return render(request,'netfix.html')
def pddtp(request):
    return render(request,'PDDTP.html')
def cctv(request):
    return render(request,'cctv.html')
def office(request):
    return render(request,'office.html')
def prog(request):
    return render(request,'prog.html')
def booking(request):
    if request.method=='POST':
        name=request.POST['name']
        fname= request.POST['father_name']
        email= request.POST['email']
        phone= request.POST['phone_num']
        gender= request.POST['gender']
        dob= request.POST['dob']
        course= request.POST['course']
        address= request.POST['address']
        photo=request.POST['photo']
        aadhar=request.POST['aadhar']
        booking_date=request.POST['booking_date']
        fee=request.POST['fee']
        a=Student(name=name,father_name=fname,email=email,phone_num=phone,gender=gender,dob=dob,course=course,address=address,photo=photo,aadhar=aadhar,booking_date=booking_date,fee=fee)
        a.save()
        return render(request,"thank_you.html")
    else:
       return render(request,"booking.html")

# views.py

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Construct the email message
            full_message = f"Name: {name}\n Email: {email}\n subject: {subject}\n Message: {message}\n"


            send_mail(
                subject,
                full_message,
                email,  # Sender's email, typically from the form
                ['aswathyar2701@gmail.com'],  # Recipient(s) of the contact form submission
                fail_silently=False,
            )
            return render(request,'thank_you.html')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})

