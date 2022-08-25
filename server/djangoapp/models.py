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
    carmake = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
