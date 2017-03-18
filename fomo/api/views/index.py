from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
from catalog import models as cmod
from django.http import HttpResponse, HttpResponseRedirect
from itertools import chain


@view_function
def process_request(request):

    lastf = request.last5
    lastfDisplay = []
    for p in lastf:

      tempProduct = cmod.Product.objects.get(id=p)


      lastfDisplay.append(tempProduct)



      print('>>>>><<<<<', lastfDisplay)


    products = cmod.Product.objects.all().order_by('name')
    # last_5 = products.filter(id = request.session['last5'])

    if request.urlparams[0] != '':
        products = products.filter(category = request.urlparams[0])


    category = cmod.Category.objects.all()

    context = {
        'products': products,
        'category': category,
        'last5': lastfDisplay
        # 'combined': result_list


    }


    # try:
    #   lastf = request.last5
    #   lastfDisplay = []
    #   for p in lastf:
    #     print(p)
    #     tempProduct = cmod.Product.objects.get(id=p)
    #     lastfDisplay.append(tempProduct)
    # except:



    return dmp_render(request, 'index.html', context)
