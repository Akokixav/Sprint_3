from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
from account import models as amod
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from formlib.form import FormMixIn
from django.contrib.auth.models import Permission, Group

from django.contrib.auth import authenticate, login

@view_function
def process_request(request):

    form = SignupForm(request)

    if form.is_valid():
        user = amod.FomoUser()
        form.commit(user)
        # login(request, form.new_user)
        return HttpResponseRedirect('/Administrator/users')


    return dmp_render(request, 'create_user.html', {'form' :form, })


class SignupForm(FormMixIn, forms.Form):
    def init(self, new_user):
        self.fields['username'] = forms.CharField(label='Username', max_length=100)
        self.fields['password'] = forms.CharField(max_length=32, widget=forms.PasswordInput)
        self.fields['first_name'] = forms.CharField(label='First Name')
        self.fields['last_name'] = forms.CharField(label='Last Name')
        self.fields['address'] = forms.CharField(label='Address')
        self.fields['zip'] = forms.CharField(label='Zip')
        self.fields['email'] = forms.EmailField(label='Email')
        self.fields['phone_number'] = forms.CharField(label='Phone Number')
        self.fields['city'] = forms.CharField(label='City')
        self.fields['state'] = forms.CharField(label='State')
        self.fields['birthday'] = forms.DateField(required = True)

    def clean_username(self):
        un = self.cleaned_data.get('username')
        users = amod.FomoUser.objects.filter(username = un).exclude(id = self.request.user.id)

        if len(users) > 0:
            raise forms.ValidationError('This username is taken')

        return un

    def commit(self, user):
        user.username = self.cleaned_data.get('username')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name  = self.cleaned_data.get('last_name')
        user.address  = self.cleaned_data.get('address')
        user.zip = self.cleaned_data.get('zip')
        user.email = self.cleaned_data.get('email')
        user.phone_number = self.cleaned_data.get('phone_number')
        user.city = self.cleaned_data.get('city')
        user.state = self.cleaned_data.get('state')
        user.set_password(self.cleaned_data.get('password'))

        user.save()

    # def commit(self, new_product):
