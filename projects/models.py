from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator 

# def current_year():     
#     return datetime.date.today().year 

# def max_value_current_year(value):     
#     return MaxValueValidator(current_year())(value)     

# Create your models here.
# STATUSES = (
#     ('Ongoing', 'Ongoing'),
#     ('Completed', 'Completed')
# )
# year = models.IntegerField(('year'), validators=[MinValueValidator(2010), max_value_current_year]) 
# status = models.CharField(max_length=10, choices=STATUSES)
class Project(models.Model):
    picture = models.ImageField(null=True)
    title = models.CharField(max_length=200)
    # brief = models.TextField()
    client = models.CharField(max_length=100)
    date = models.DateField(null=True)
    services_offered = models.TextField(null=True)
    duration = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Photo(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name="photos")
    image = models.ImageField()

    def __str__(self):
        return self.project.image


class FeaturedProject(models.Model):
    project = models.ForeignKey('Project', blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.project.name if self.project else 'UNASIGNED'