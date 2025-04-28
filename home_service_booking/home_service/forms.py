from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Booking
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class BookingForm(forms.ModelForm):
    booking_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})  # 🗓 Adds a date picker
    )

    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'area', 'location', 'street', 'house_no', 'booking_date']
