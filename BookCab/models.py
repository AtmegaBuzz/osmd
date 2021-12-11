from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class CabGroup(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    
    
class Booking(models.Model):
    
    destination = models.CharField(max_length=50,blank=False,null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="user")
    status = models.PositiveIntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(3)])  
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    group = models.ForeignKey(CabGroup,on_delete=models.CASCADE,null=True,blank=True)
    cost = models.PositiveIntegerField(blank=True,null=True)
    distance = models.PositiveIntegerField(blank=True,null=True)
    
    def __str__(self):
        return f"{self.user} {self.destination} {self.status} {self.user.id}"
    
