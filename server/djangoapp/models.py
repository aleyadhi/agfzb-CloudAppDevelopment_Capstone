from django.db import models
from django.utils.timezone import now


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return "CarMake: " + self.name + "," + \
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
    name = models.CharField(max_length=20)
    dealerid = models.IntegerField()
    year = models.DateField()
    carmake = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    def __str__(self):
        return "Car Make: " + self.carmake + "," + \
                "Name: " + self.name + "," + \
                "Dealer ID: " + self.dealerid + "," + \
                "Year: " + str(self.year) 


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
    class CarDealer:
        def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
            # Dealer address
            self.address = address
            # Dealer city
            self.city = city
            # Dealer Full Name
            self.full_name = full_name
            # Dealer id
            self.id = id
            # Location lat
            self.lat = lat
            # Location long
            self.long = long
            # Dealer short name
            self.short_name = short_name
            # Dealer state
            self.st = st
            # Dealer zip
            self.zip = zip

        def __str__(self):
            return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
    class DealerReview:
        def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment, id):
            self.dealership = dealership
            self.name = name
            self.purchase = purchase
            self.review = review
            self.purchase_date = purchase_date
            self.car_make = car_make
            self.car_model = car_model
            self.car_year = car_year
            self.sentiment = sentiment
            self.id = id

        def __str__(self):
            return "Dealer name: " + self.review