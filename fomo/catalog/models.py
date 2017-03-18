from django.db import models
from polymorphic.models import PolymorphicModel

#Catalog Models

# Create your models here.


class Category(models.Model):
    #id
    name = models.TextField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(PolymorphicModel):
    #id
    price = models.DecimalField(max_digits=8, decimal_places=2) #999, 999.99
    name = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    category = models.ForeignKey('Category')
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)



class BulkProduct(Product):
    #id
    serial_number = models.TextField(blank=True)
    quantity = models.IntegerField()
    reorder_trigger = models.IntegerField()
    reorder_quantity = models.IntegerField()


class UniqueProduct(Product):
    #id
    serial_number = models.TextField(blank=True)
    #vendor

class RentalProduct(Product):
    #id
    serial_number = models.TextField(blank=True)



#Product (Abstract class)
    #picture
class ProductPictures(models.Model):
    product = models.ForeignKey('Product', related_name = 'pictures')
    subdir = models.TextField(blank=True, null=True)
    alttext = models.TextField(blank=True, null=True)
    minetype = models.TextField(blank=True, null=True)
        #image/jpg, image/png, image/gif


#Normal inheritance with all concrete classes
#Can create just
