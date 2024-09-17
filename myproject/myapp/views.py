# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('psw')
        
        # Check if the user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'User with this username already exists.')
            return redirect('login')
        
        # Create the user
        user = User.objects.create(username=username, email=email, phone=phone, password=password)
        
        # You can add additional logic here, such as logging the user in automatically
        
        # Redirect to success page or any other desired page
        return redirect('success')

    return render(request, 'login.html')

def success(request):
    return render(request, 'success.html')
