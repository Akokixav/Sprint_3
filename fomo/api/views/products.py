from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from django_mako_plus import view_function
import json
from .. import dmp_render, dmp_render_to_string
from catalog import models as cmod
from django import forms
from formlib.form import FormMixIn

@view_function
def process_request(request):
    # Create a list to hold the dictionaries
    dlist = []

    try:
        urlProduct = request.GET.get('product')
        urlCategory = request.GET.get('category')
        urlMin = request.GET.get('min-price')
        urlMax = request.GET.get('max-price')

        # grab all the products to begin with
        qry = cmod.Product.objects.all()


        # then filter them according to the url parameters
        if urlProduct is not None:
            qry = qry.filter(name__icontains=urlProduct)
        if urlCategory is not None:
            qry = qry.filter(category__name__icontains=urlCategory)
        if urlMin is not None:
            qry = qry.filter(price__gte=urlMin)
        if urlMax is not None:
            qry = qry.filter(price__lte=urlMax)




        # grab all products based on the above filters
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        for p in qry:
            # Create the dictionary itself, this variable will change throughout the loop
            d = {}
            d['name'] = p.name
            d['category'] = p.category.name
            d['price'] = p.price
            if hasattr(p, 'quantity'):
                d['quantity'] = p.quantity
            if hasattr(p, 'reorder_trigger'):
                d['reorder-trigger'] = p.reorder_trigger
            if hasattr(p, 'reorder_quantity'):
                d['reorder_quantity'] = p.reorder_quantity
            if hasattr(p, 'serial_number'):
                d['serial_number'] = p.serial_number
            dlist.append(d)
    except:
        #return HttpResponseNotFound('Invalid Details')
        dlist = [{'Error in the api call'}]

    print('------- d list: ', dlist)

    [ { 'error': '...' }, ]

    # return HttpResponse(json.dumps(ret), content_type='application/json')
    return JsonResponse(dlist, safe=False)
    #wrap a list into a dictionary and return that 
