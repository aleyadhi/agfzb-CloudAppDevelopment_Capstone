from django.contrib import admin
from .models import CarModel, CarMake


# Register your models here.
    
# CarModelInline class
# class CarModelInline(admin.StackedInline):
#     model = CarModel
#     extra = 5

# # CarModelAdmin class
# class CarModelAdmin(admin.ModelAdmin):
#     list_display = ['carmake', 'name', 'dealerid', 'year']

# # CarMakeAdmin class with CarModelInline
# class CarMakeAdmin(admin.ModelAdmin):
#     inlines = [CarModelInline]
#     list_display = ['name']

# Register models here
admin.site.register(CarMake)
admin.site.register(CarModel)