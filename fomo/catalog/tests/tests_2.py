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


    def test_polymorphism(self):
        """Test polymorphism of products """
        ##Creates categories
        cat1 = cmod.Category()
        cat1.code = 'brass'
        cat1.name = 'Brass Instruments'
        cat1.save()

        cat2 = cmod.Category()
        cat2.code = 'woodwind'
        cat2.name = 'Woodwind Instruments'
        cat2.save()

        cat3 = cmod.Category()
        cat3.code = 'string'
        cat3.name = 'String Instruments'
        cat3.save()


        #Creates conditions
        con1 = cmod.Condition()
        con1.name = 'Poor'
        con1.save()

        con2 = cmod.Condition()
        con2.name = 'Good'
        con2.save()

        con3 = cmod.Condition()
        con3.name = 'Excellent'
        con3.save()


        ##Creates a unique product
        up1 = cmod.UniqueProduct()
        up1.category = cat1
        up1.name = 'Trumpet'
        up1.brand = 'Yamaha'
        up1.price = Decimal('899.99')
        up1.serial_number = '747amfhuefhi'
        up1.save()

        ##Creates a rental product
        rp1 = cmod.RentalProduct()
        rp1.category = cat3
        rp1.name = 'Trombone'
        rp1.brand = 'Yamaha'
        rp1.price = Decimal('1029.99')
        rp1.serial_number = '0348dsaiopjd'
        rp1.condition = con2
        rp1.save()



        #pull back off of the database
        brand1 = up1.brand
        brand2 = rp1.brand
        self.assertEqual(brand1, brand2)
