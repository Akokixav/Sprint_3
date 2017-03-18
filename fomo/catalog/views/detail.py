from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
import random
from account import models as amod
from catalog import models as cmod
from django.http import HttpResponse, HttpResponseRedirect

@view_function
def process_request(request):
    pid = request.urlparams[0]

    try:
        product = cmod.Product.objects.get(id=pid)

    except cmod.Product.DoesNotExist:
        return HttpResponseRedirect('/catalog/index')

    #add to the last 5 viewed items
    if pid in request.last5:
        request.last5.remove(pid)

    request.last5.insert(0, product.id)


    print('PPPPPPPPP',request.last5)

    context = {
        'product': product,


    }


    return dmp_render(request, 'detail.html',context)


##############AJAX VERSION ################

@view_function
def modal(request):

    # print('>>>>>>>>>')
    # product = cmod.Product.objects.get(id=7)
    #
    #
    # context = {
    # 'product': product
    # }


        #if not authenticated
    return dmp_render(request, 'detail.modal.html')
