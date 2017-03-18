from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
from catalog import models as cmod
from django.http import HttpResponse, HttpResponseRedirect
from formlib.form import FormMixIn
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
# from formlib.form import FormMixIn
from django import forms

@view_function
@login_required(login_url='/account/login_class/')
@permission_required('catalog.change_product', login_url='/Administrator/products/')
def process_request(request):

    try:
        product = cmod.Product.objects.get(id=request.urlparams[0])
    except cmod.Product.DoesNotExist:
        return HttpResponseRedirect('/Administrator/products')

    #UNDERSTAND
    form = EditProductForm(request,product=product, initial ={
        'name': product.name,
        'category': product.category,
        'price': product.price,
        'quantity': getattr(product, 'quantity', 0)

    })


    # form = MyForm(request)
    if form.is_valid():
        form.commit(product)
        return HttpResponseRedirect('/Administrator/products')

    context = {
        'product': product,
        'form': form,
    }
    return dmp_render(request, 'product.html', context)

class EditProductForm(FormMixIn, forms.Form):

    def init(self, product):
        self.fields['name'] = forms.CharField(label='productname', max_length=100)
        self.fields['category'] = forms.ModelChoiceField(label='category', queryset = cmod.Category.objects.order_by('name').all())
        self.fields['price'] = forms.DecimalField(label='Price')
        if hasattr(product, 'quantity'):
            self.fields['quantity'] = forms.IntegerField(label = 'Quantity')


    def commit(self, product):
        product.name = self.cleaned_data.get('name')
        product.category = self.cleaned_data.get('category')
        product.price = self.cleaned_data.get('price')
        product.quantity = self.cleaned_data.get('quantity')
        product.save()

            #print(form.cleaned_data.get('price'))


################################################


@view_function
@permission_required('catalog.delete_product', login_url='/Administrator/products/')
def delete(request):
    try:
        product = cmod.Product.objects.get(id=request.urlparams[0])
    except cmod.Product.DoesNotExist:
        return HttpResponseRedirect('/Administrator/products/')

        print('>>>>>>>>>>>', 'Im working')

    product.delete()
    return HttpResponseRedirect('/Administrator/products/')


#############################################
