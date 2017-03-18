# from django import settings
from django.http import HttpResponseRedirect, HttpResponse
from django_mako_plus import view_function
from django.core.context_processors import csrf
from django.shortcuts import get_object_or_404, render

from .. import dmp_render, dmp_render_to_string

@view_function
def process_request(request):
    print('I am Here Stephane')

    # return dmp_render(request, 'contact.html', {})
    return render(request, 'contact.html', {})
