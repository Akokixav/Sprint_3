from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
from account import models as amod
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from formlib.form import FormMixIn
from django.contrib.auth.models import Permission, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

@view_function
@permission_required('account.View_users', login_url='/homepage/index/')
@login_required(login_url='/account/login_class/')
def process_request(request):

#Pull all users from the database
    users = amod.FomoUser.objects.all()

    context = {
        'userlist': users,

    }
    return dmp_render(request, 'users.html', context)


################################################


@view_function
@permission_required('catalog.change_product', login_url='/Administrator/users/')
def edit(request):
    user = amod.FomoUser.objects.get(id=request.urlparams[0])

    form = EditProductForm(request, initial ={
        'username': user.username,
        'first_name': user.first_name,
        'last_name' : user.last_name,
        'address': user.address,
        'zip': user.zip,
        'email': user.email,
        'phone_number': user.phone_number,
        'city': user.city,
        'state': user.state,
        'permission': user.user_permissions.all(),
        'groups': user.groups.all(),

    })


    if form.is_valid():
        form.commit(user)
        return HttpResponseRedirect('/Administrator/users')

    context = {
        'uniqueuser': user,
        'form': form,
    }

    return dmp_render(request, 'edit.html', context)

class EditProductForm(FormMixIn, forms.Form):

        def init(self):
            self.fields['username'] = forms.CharField(label='Username', max_length=100)
            self.fields['groups'] = forms.ModelMultipleChoiceField(label='Group',
            queryset=Group.objects.order_by('name').all(), required=False)
            self.fields['permissions'] = forms.ModelMultipleChoiceField(label="Permissions", required=False,
            queryset=Permission.objects.all(), help_text='Hold control to select multiple permissions.')
            self.fields['first_name'] = forms.CharField(label='First Name')
            self.fields['last_name'] = forms.CharField(label='Last Name')
            self.fields['address'] = forms.CharField(label='Address')
            self.fields['zip'] = forms.CharField(label='Zip')
            self.fields['email'] = forms.EmailField(label='Email')
            self.fields['phone_number'] = forms.CharField(label='Phone Number')
            self.fields['city'] = forms.CharField(label='City')
            self.fields['state'] = forms.CharField(label='State')


        #     self.fields['group'] = forms.ModelMultipleChoiceField(label="Group",required=False, queryset = Group.objects.all(),
        # widget=forms.CheckboxSelectMultiple(attrs={'class':'form-control'}))


        def clean_username(self):
            un = self.cleaned_data.get('username')
            users = amod.FomoUser.objects.filter(username = un).exclude(id = self.request.urlparams[0])

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

            # for group in self.cleaned_data.get('group'):
            #     user.groups.add(group)

            user.save()

            user.user_permissions.set(self.cleaned_data.get('permissions'))
            user.groups.set(self.cleaned_data.get('groups'))

################################################
@view_function
@permission_required('catalog.delete_fomouser', login_url='/Administrator/users/')
def delete(request):
    try:
        user = amod.FomoUser.objects.get(id=request.urlparams[0])
    except amod.FomoUser.DoesNotExist:
        return HttpResponseRedirect('/Administrator/users/')

    user.delete()
    return HttpResponseRedirect('/Administrator/users/')
