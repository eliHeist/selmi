from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=25)
    company = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    
    info = models.TextField(verbose_name='How can we help you?') 
    is_attended_to = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self) -> str:
        return self.name