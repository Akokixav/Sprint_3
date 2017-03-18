from django.conf import settings
from django import forms
# from django import settings
from django.http import HttpResponseRedirect
from .. import dmp_render, dmp_render_to_string
from django_mako_plus import view_function
from formlib.form import FormMixIn
from catalog import models as cmod
from catalog.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required



@view_function
@permission_required('catalog.add_product', login_url='/Administrator/products/')
def process_request(request):


    form = ContactForm(request)
    if form.is_valid():

        #new_product = cmod.UniqueProduct()

        form.commit(new_product)

        print('>>>>> FORM CHECK OUT')
        return HttpResponseRedirect('/Administrator/products/')

        form = ContactForm()

    return dmp_render(request, 'newproduct.html', {'form' :form, })


class ContactForm(FormMixIn, forms.Form):



    def init(self, new_product):
        self.fields['name'] = forms.CharField(label='Name', max_length=100)
        self.fields['brand'] = forms.CharField(label='Brand', max_length=100)
        self.fields['category'] = forms.ModelChoiceField(label='Category', queryset = cmod.Category.objects.order_by('name').all())
        self.fields['producttype'] = forms.ChoiceField(label="Product Type", choices=[
            ['unique', 'Unique Product'],
            ['bulk', 'Bulk Product'],
            ['rental', 'Rental Product'],

        ], initial ="unique")

        self.fields['serial_number'] = forms.CharField(label='Serial Number', max_length=100)
        self.fields['price'] = forms.DecimalField(label='Price')
        self.fields['quantity'] = forms.DecimalField(label='Quantity', widget=forms.TextInput(attrs={'class': 'producttype-quantity'}))

        self.fields['reoderpoint'] = forms.DecimalField(label='Reorder point', widget=forms.TextInput(attrs={'class': 'producttype-rp'}))
        self.fields['reoderquantity'] = forms.DecimalField(label='Reorder Quantity', widget=forms.TextInput(attrs={'class': 'producttype-rq'}))
        self.fields['category'] = forms.ModelChoiceField(label='Products', queryset = cmod.Category.objects.order_by('name').all())

        self.fields['quantity'].required = False
        self.fields['reoderquantity'].required = False
        self.fields['reoderpoint'].required = False



    def commit(self, new_product):
        print('>>>>>>>>> WORKING?')

        myproduct = self.cleaned_data.get('producttype')
        if myproduct == "bulk":
            new_product = cmod.BulkProduct()
        elif myproduct == "unique":
            new_product = cmod.UniqueProduct()
        else:
            new_product = cmod.RentalProduct()

        new_product.name = self.cleaned_data.get('name')
        new_product.category = self.cleaned_data.get('category')
        new_product.price = self.cleaned_data.get('price')
        new_product.quantity = self.cleaned_data.get('quantity')
        new_product.reorder_trigger = self.cleaned_data.get('reoderpoint')
        new_product.reorder_quantity = self.cleaned_data.get('reoderquantity')
        new_product.serial_number = self.cleaned_data.get('serial_number')
        new_product.save()
        #return the value
