from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
from account import models as amod
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from formlib.form import FormMixIn
from django.contrib.auth.decorators import login_required

@view_function
@login_required(login_url='/account/login_class/')
def process_request(request):
    user = amod.FomoUser.objects.get(id=request.user.id)

    form = Edituser(request, initial ={
        'username': user.username,
        'first_name': user.first_name,
        'last_name' : user.last_name,
        'address': user.address,
        'zip': user.zip,
        'email': user.email,
        'phone_number': user.phone_number,
        'city': user.city,
        'state': user.state,
    })

    if form.is_valid():
        form.commit(user)
        return HttpResponseRedirect('/account/index')

    return dmp_render(request, 'edit.html', {'form' :form, })


class Edituser(FormMixIn, forms.Form):

        def init(self):
            self.fields['username'] = forms.CharField(label='Username', max_length=100)
            self.fields['first_name'] = forms.CharField(label='First Name')
            self.fields['last_name'] = forms.CharField(label='Last Name')
            self.fields['address'] = forms.CharField(label='Address')
            self.fields['zip'] = forms.CharField(label='Zip')
            self.fields['email'] = forms.EmailField(label='Email')
            self.fields['phone_number'] = forms.CharField(label='Phone Number')
            self.fields['city'] = forms.CharField(label='City')
            self.fields['state'] = forms.CharField(label='State')

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
            # user.set_password(self.cleaned_data.get('password'))

            user.save()
