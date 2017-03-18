from django.conf import settings
from django import forms
# from django import settings
from django.http import HttpResponseRedirect
from .. import dmp_render, dmp_render_to_string
from django_mako_plus import view_function
from account.models import FomoUser
from datetime import datetime

@view_function
def process_request(request):


form = createUserForm(request,product=product, initial ={
    'name': product.name,
    'category': product.category,
    'price': product.price,
    'quantity': getattr(product, 'quantity', 0)

})

class createUserForm(FormMixIn, forms.Form):

    def init(self):
        self.fields['name'] = forms.CharField(label='productname', max_length=100)
        self.fields['category'] = forms.ModelChoiceField(label='category', queryset = cmod.Category.objects.order_by('name').all())
        self.fields['price'] = forms.DecimalField(label='Price')

    
