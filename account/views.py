from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact,Course,Staff
from django.contrib import messages

# Create your views here.

def mainhome(request):
    return render(request,'mainhome.html')

def index(request):
    if request.method=="POST":
      email=request.POST['email']
      password=request.POST['password']
      try:
        check_user=Staff.objects.get(email=email,password=password) 
        request.session['email']=check_user.email
        request.session['name1']=check_user.name1
        request.session['phno']=check_user.phno
        return redirect('home')
      except Staff.DoesNotExist:
        messages.error(request,'Invalid username or password')
        return redirect('index')
    return render(request,'index.html')

def signup(request):
    if request.method == "POST":
        name1 = request.POST['name1']
        name2 = request.POST['name2']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        phno = request.POST['phno']
        day = request.POST['day']
        month = request.POST['month']
        year = request.POST['year']
        radio= request.POST['radio']
        if password == password2 :
            if Staff.objects.filter(email = email).exists():
                messages.info(request,'Email Taken')
                return redirect('signup')
            else:
                customer = Staff.objects.create(email = email,name1 = name1,name2 = name2,password = password,phno = phno,day = day,month = month,year = year,radio = radio)
                customer.save()
                messages.info(request,'user created')
                return redirect('login')
        else:
            messages.info(request,'password is not match') 
            return redirect('signup')       
    else:        
        return render(request,'signup.html')


def gallery(request):
    return render(request,'gallery.html')

def forget(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        if Staff.objects.filter(email=email).exists():
            Staff.objects.filter(email=email).update(password=password)
            return redirect('login')
        else:
            messages.error(request,'invalid data')
            return redirect('forgetpassword')    
    return render(request,'forgetpassword.html') 
       



def contact(request):
    if request.method=="POST":
        if request.POST['name'] is not None:
            enq=Contact.objects.create(name=request.POST['name'],email=request.POST['email'],phno=request.POST['phno'])
            enq.save()
            dicts={'out':1,'name':request.POST['name']}
            return render(request,'contact.html',dicts)
    return render(request,'contact.html') 

def course(request):
  courses={
  'course':Course.objects.all()
  }
  return render(request,'course.html',courses)  
  
    
# def mainhome(request):

#     if request.method == "POST":
#         email = request.POST['email']
#         password = request.POST['password']
#         if Staff.objects.filter(email=email).exists():
#             Staff.objects.filter(email=email).update(password=password)
#             return redirect('signup')
#         else:
#             messages.error(request,'invalid data')
#             return redirect('forgetpassword')
#     return render(request,'forgetpassword.html')  