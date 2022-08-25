from django.db import models
from django.utils.timezone import now


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)

def __str__(self):
    return "CarMake: " + slef.name + "," + \
            "Description: " + self.description

class CarModel(models.Model):
    SEDAN = 'sedan'
    SUV = 'suv'
    WAGON = 'wagon'
    NAME_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'Suv'),
        (WAGON, 'Wagon')
    ]
    carmake = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, choices=NAME_CHOICES)
    dealerid = models.IntegerField()
    year = models.DateField()

def __str__(self):
    return "Car Make: " + self.carmake + "," + \
            "Name: " + self.name + "," + \
            "Dealer ID: " + self.dealerid + "," + \
            "Year: " + str(self.year) 


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
