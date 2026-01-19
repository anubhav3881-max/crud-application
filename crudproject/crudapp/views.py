from django.shortcuts import render, redirect,HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='login')
def addmissionpage(request):
    if(request.method=="POST"):
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        image = request.FILES.get('image')
        userid=request.user
        
        addmission=Addmission(name=name,email=email,contact=contact,address=address,dob=dob,image=image, userid=userid)
        addmission.save()
        # yha pr changes
        msg={"success":"Form submitted successfully!"}
        return JsonResponse(msg)

        # return render(request, 'addmission.html',{'success':"form submitted successfully!"})
    return render(request, 'addmission.html')

@login_required(login_url='login')
def updatepage(request):
    
    if(request.method=='POST'):
        name=request.POST.get('name')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        image = request.FILES.get('image')
        id= request.POST.get('userid')
        data= Addmission.objects.get(id=id)
        
        data.name=name
        data.email=email
        data.contact=contact
        data.address=address
        data.dob=dob
        data.image=image
        data.save()
        msg={"success":"Form Updated successfully!"}
        return JsonResponse(msg)
       

        # return redirect('display')#,{'successsuccessfully!"}
        # return render (request, 'update.html',{'success':"Form updated successfully!"})
    return render(request, 'update.html')
def signuppage(request):
    if(request.method=="POST"):
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        if(password!=confirmpassword):
            return JsonResponse({'error':"password and confirm password does not match!"})
         # 2. Check if Username already exists
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': "Username already exists!"}, status=400)

        # 3. Check if Email already exists (Optional but recommended)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': "Email already registered!"}, status=400)

        # 4. User Create Karein
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return JsonResponse({'success': "Your Account has been created successfully!"}, status=200)
        except Exception as e:
            return JsonResponse({'error': "Something went wrong: " + str(e)}, status=500)
    return render(request, 'signup.html')
def loginpage(request):
    if(request.method=="POST"):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if(user is not None):
            login(request, user)
            return JsonResponse({"success":True})
        else:
            return render(request, 'login.html', {'error':"invalid credentials!"})
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def displaypage(request):
    data=Addmission.objects.filter(userid=request.user)
    return render(request, 'display.html',{'data':data})

def deleterecord(request, id):
    data=Addmission.objects.get(id=id)
    data.delete()
    return redirect('display')
def editrecord(request, id):
    record=Addmission.objects.get(id=id)
    return render(request, 'update.html', {'data':record})
