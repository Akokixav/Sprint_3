from django.test import TestCase
from account import models as amod
from account.models import FomoUser
from datetime import datetime
from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from catalog import models as cmod
from django.http import HttpResponseRedirect, HttpResponse
from formlib.form import FormMixIn
from django import forms
from account.models import FomoUser
from decimal import Decimal

from django.contrib.auth import authenticate, login

# from myapp.models import Animal

class ProductTest(TestCase):
    # def setUp(self):
    #     Animal.objects.create(name="lion", sound="roar")
    #     Animal.objects.create(name="cat", sound="meow")

    def test_product_picture(self):
        """Test the foreign key picture to products"""
        #creates a category
        cat3 = cmod.Category()
        cat3.code = 'string'
        cat3.name = 'String Instruments'
        cat3.save()

        # Creates a bulk product
        bp1 = cmod.BulkProduct()
        bp1.category = cat3
        bp1.name = 'Guitar Strings'
        bp1.brand = 'Gibson'
        bp1.price = Decimal('9.99')
        bp1.quantity = 40
        bp1.reorder_trigger = 10
        bp1.reorder_quantity = 35
        bp1.save()

        #Creates a picture and is a foreign key to the bulk product
        pic1 = cmod.ProductPicture()
        pic1.product = bp1
        pic1.path = 'catalog/media/product_images/gibsonStrings.jpg'
        pic1.altText = 'Guitar Strings1'
        pic1.imageType = 'jpg'
        pic1.save()

        #pull back off of the database
        product1 = cmod.Product.objects.get(id=1)
        picture1path = product1.pictures.all()[0].path
        picture2path = bp1.pictures.all()[0].path
        self.assertEqual(picture1path, picture2path)
