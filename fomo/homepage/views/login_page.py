from django.conf import settings
from django import forms
# from django import settings
from django.http import HttpResponseRedirect
from .. import dmp_render, dmp_render_to_string
from django_mako_plus import view_function
from django.contrib.auth import authenticate, login


@view_function
def process_request(request):

     if request.method == 'POST':
         form = ContactForm(request.POST)
         if form.is_valid():

             print('>>>>> FORM CHECK OUT')
             user = authenticate(username = request.POST.get('username'), password = request.POST.get('password'))

             #log the user in
             if user is not None:
                 login(request, user)
                 return HttpResponseRedirect('/homepage/index/')
     else:
        form = ContactForm()

        return dmp_render(request, 'login_page.html', {'form' :form, })


class ContactForm(forms.Form):

    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)


    def clean_name(self):
        name = self.cleaned_data.get('name')
        #do validation
        parts = name.strip().split()
        if len(parts) <=1:
            # print('>>>>>>>>>')
            # # raise forms.ValidationError('Please...')

            raise forms.ValidationError("That URL is already in the database.  Please submit a unique URL.")
            # #return value
            # print('>>>>>>>>> I"M WORKING')
        return name

        #return the value
