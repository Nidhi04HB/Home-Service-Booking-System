"""from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('service/<int:service_id>/', views.service_detail, name='service_detail'),
    path('book/<int:service_id>/', views.book_service, name='book_service'),
    path('success/', views.booking_success, name='booking_success'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
]"""

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect



def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

urlpatterns = [
    path('', views.dashboard, name='home'),  # Change 'home' to 'dashboard'
    path('service/<int:service_id>/', views.service_detail, name='service_detail'),
    path('book/<int:service_id>/', views.book_service, name='book_service'),
    path('success/', views.booking_success, name='booking_success'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    ]
def redirect_to_login(request):
    return redirect("/login/")

urlpatterns += [
    path("accounts/login/", redirect_to_login),
]