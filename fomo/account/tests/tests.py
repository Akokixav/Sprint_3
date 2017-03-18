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

from django.contrib.auth import authenticate, login

# from myapp.models import Animal

class FomoUserTest(TestCase):
    # def setUp(self):
    #     Animal.objects.create(name="lion", sound="roar")
    #     Animal.objects.create(name="cat", sound="meow")

    def test_creating_users(self):
        """Test the creation of a few fomouser objects"""
        # Creates the users
        user1 = FomoUser()
        user1.first_name = 'Stephane'
        user1.last_name = 'Akoki'
        user1.set_password('baseball')
        user1.date_joined = datetime.now()
        user1.last_login = datetime.now()
        user1.username = 'yakoki'
        user1.email = 'yakoki@byu.edu'
        user1.phone = '336-486-4595'
        user1.address = '1960 N Canyon Rd'
        user1.city = 'Provo'
        user1.state = 'Utah'
        user1.zip_code = '84604'
        user1.is_superuser = True
        user1.is_staff = True
        user1.is_active = True
        user1.save()


        #pull back off of the database
        u2 = FomoUser.objects.get(username='yakoki')
        self.assertEqual(user1.first_name, u2.first_name)




    def test_authenticating_users(self):
        """Tests the authentication of users"""
        # Creates the users
        user1 = FomoUser()
        user1.first_name = 'Stephane'
        user1.last_name = 'Akoki'
        user1.set_password('baseball')
        user1.date_joined = datetime.now()
        user1.last_login = datetime.now()
        user1.username = 'yakoki'
        user1.email = 'yakoki@byu.edu'
        user1.phone = '336-486-4595'
        user1.address = '1960 N Canyon Rd'
        user1.city = 'Provo'
        user1.state = 'Utah'
        user1.zip_code = '84604'
        user1.is_superuser = True
        user1.is_staff = True
        user1.is_active = True
        user1.save()


        #pull back off of the database
        user1auth = authenticate(username = user1.username, password='baseball')
        u2 = FomoUser.objects.get(username='yakoki')
        self.assertEqual(u2, user1auth)
