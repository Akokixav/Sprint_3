from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
from account import models as amod
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from formlib.form import FormMixIn
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required

@view_function
@login_required(login_url='/account/login_class/')
def process_request(request):
    user = amod.FomoUser.objects.get(id=request.user.id)
    form = Edituser(request)

    if form.is_valid():
        form.commit(user)
        login(request, form.user)
        return HttpResponseRedirect('/account/index')

    return dmp_render(request, 'edit.html', {'form' :form, })


class Edituser(FormMixIn, forms.Form):

        def init(self):
            self.fields['oldpassword'] = forms.CharField(max_length=32, widget=forms.PasswordInput)
            self.fields['newpassword'] = forms.CharField(max_length=32, widget=forms.PasswordInput)
            self.fields['confirmpassword'] = forms.CharField(max_length=32, widget=forms.PasswordInput)

        def clean_oldpassword(self):
            self.user = authenticate(username = self.request.user.username, password = self.cleaned_data.get('oldpassword'))
            if self.user is None:
                raise forms.ValidationError('Invalid password')

        def clean(self):
            p1 = self.cleaned_data.get('newpassword')
            p2 = self.cleaned_data.get('confirmpassword')

            if (p2 != p1):
                raise forms.ValidationError('Password do not match')

        def commit(self, user):
            user.set_password(self.cleaned_data.get('newpassword'))



            user.save()
            self.user = authenticate(username = self.request.user.username, password = self.cleaned_data.get('oldpassword'))
