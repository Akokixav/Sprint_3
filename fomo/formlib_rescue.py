from django.conf import settings
from django import forms
# from django import settings
from django.http import HttpResponseRedirect
from .. import dmp_render, dmp_render_to_string
from django_mako_plus import view_function
from formlib.form import FormMixIn



@view_function
def process_request(request):

    #  if request.method == 'POST':
    form = ContactForm(request)
    if form.is_valid():
        form.commit()

        print('>>>>> FORM CHECK OUT')
        return HttpResponseRedirect('/homepage/forms/')
    #  else:
        form = ContactForm()

    return dmp_render(request, 'forms.html', {'form' :form, })


class ContactForm(FormMixIn, forms.Form):
    SUBJECT_CHOICES = [
        ['payment', 'Payment issue'],
        ['login', 'I cant login'],
        ['technical', 'Payment issue'],
        ['upset', 'Payment issue'],
    ]


    def init(self):
        self.fields['name'] = forms.CharField(label='name', max_length=100)
        self.fields['email'] = forms.EmailField(label='Email', max_length=100)
        self.fields['message'] = forms.CharField(label='message', max_length=1000, widget=forms.Textarea())
        self.fields['Subject'] = forms.ChoiceField(label="subject", choices = ContactForm.SUBJECT_CHOICES)

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

    def commit(self):
        email = self.cleaned_data.get('email')
        print('>>>>>>>>> WORKING?')
        #return the value
