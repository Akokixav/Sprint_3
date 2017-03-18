from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
from catalog import models as cmod
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

@view_function
# @permission_required('account.delete_product', login_url='/homepage/index/')
@permission_required('account.View_users', login_url='/homepage/index/') 
@login_required(login_url='/account/login_class/')

def process_request(request):

#Pull all products from the database
    products = cmod.Product.objects.order_by('name').all()

    # .all() RETURN LISTS
    # .filter()
    # .exclude()

    # try:

    #.p = cmod.Product.objets.get(id=00000) return a single object
    # except cmod.Product.DoesNotExist:
    #     return HttpResponse('Does not exist')
    #     return HttpResponseRedirect('/manager/products/')
    #     return HttpResponse(status=404)

    #render the template
    context = {
        'products': products,

    }
    return dmp_render(request, 'products.html', context)

@view_function
def get_quantity(request):
    # return the curent quantity for a given product id
    pid = request.urlparams[0]
    try:
        product = cmod.BulkProduct.objects.get(id=request.urlparams[0])
    except cmod.BulkProduct.DoesNotExist:
        return HttpResponseRedirect('/Administrator/products')
    return HttpResponse(product.quantity)
