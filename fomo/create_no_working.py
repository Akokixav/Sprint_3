
from django.conf import settings
from django import forms
# from django import settings
from django.http import HttpResponseRedirect
from .. import dmp_render, dmp_render_to_string
from django_mako_plus import view_function
from formlib.form import FormMixIn


@view_function
def process_request(request):


         form = ContactForm(request.POST)
         if form.is_valid():

             print('>>>>> FORM CHECK OUT')
            #  print(form.cleaned_data)

             print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.')
             return HttpResponseRedirect('/Administrator/newproduct')

             form = ContactForm()

         return dmp_render(request, 'newproduct.html', {'form' :form, })


class ContactForm(FormMixIn, forms.Form):
    SUBJECT_CHOICES = [
        ['payment', 'Payment issue'],
        ['login', 'I cant login'],
        ['technical', 'Payment issue'],
        ['upset', 'Payment issue'],
    ]

    def init(self):
        self.fields['name'] = forms.CharField(label='name', max_length=100)
        self.fields['contacttype'] = forms.EmailField(label='Email', max_length=100)
        self.fields['message'] = forms.CharField(label='message', max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control'}))
        self.fields['Subject'] = forms.ChoiceField(label="subject", choices = SUBJECT_CHOICES)


        #return the value
