# from django import settings
from django.conf import settings
from django import forms
# from django import settings
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .. import dmp_render, dmp_render_to_string
from django_mako_plus import view_function
from account import models as amod
import json


@view_function
def process_request(request):
    try:
        user = amod.FomoUser.objects.get(id=request.urlparams[0])
    except: amod.FomoUser.DoesNotExist
        return HttpResponseNotFound


    ret = {
        'firstname': user.first_name,
        'lastname': user.last_name,
    }

    print('!!!!', request.GET.get('a'))


    # return HttpResponse(json.dumps(ret), content_type = "application/json")
    return JsonResponse(ret)
