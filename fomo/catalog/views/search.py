from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
from catalog import models as cmod
from django.http import HttpResponse, HttpResponseRedirect


@view_function
def process_request(request):

    # products = cmod.Product.objects.all()
    instrument = request.POST.get('instrument')
    # print('>>>>>', instrument)
    searchedProducts = cmod.Product.objects.all().filter(name__icontains=instrument)

    if len(searchedProducts) == 0:
        print('Product not found')
    print('>>>>>>>>>>>', searchedProducts)


    context = {
        'products': searchedProducts,

    }







    return dmp_render(request, 'search.html', context)
