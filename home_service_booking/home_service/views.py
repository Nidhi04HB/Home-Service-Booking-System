from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Service, Booking
from .forms import UserRegistrationForm, BookingForm
from .models import Service
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Booking

def dashboard(request):
    services = Service.objects.all()
    return render(request, 'dashboard.html', {'services': services})  # ✅ Ensure template name is correct
def home(request):
    services = Service.objects.all()
    return render(request, 'home.html', {'services': services})
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def dashboard(request):
    services = Service.objects.all()
    return render(request, 'dashboard.html', {'services': services})

"""def book_service(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'book_service.html', {'form': form})"""
@login_required
def book_service(request, service_id):  # ✅ Add 'service_id' as a parameter
    service = get_object_or_404(Service, id=service_id)  # ✅ Fetch service by ID

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # ✅ Ensure booking is linked to the logged-in user
            booking.service = service
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()

    return render(request, 'book_service.html', {'form': form, 'service': service})

def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking_list.html', {'bookings': bookings})

# Create your views here.
def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'service_detail.html', {'service': service})
from django.shortcuts import render

def booking_success(request):
    return render(request, 'booking_success.html')
#@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user) # Fetch user's bookings
    return render(request, 'my_bookings.html', {'bookings': bookings})