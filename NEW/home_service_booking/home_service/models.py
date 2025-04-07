from django.db import models
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User  
class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ✅ Must be linked to a user
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    area = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_no = models.CharField(max_length=10)
    booking_date = models.DateField(default=now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.name} for {self.service.name}"

# Create your models here.
