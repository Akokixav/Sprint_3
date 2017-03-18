from django.conf import settings

from django_mako_plus import view_function

import requests

@view_function
def process_request(request):

    r = requests.get('api.openweathermap.org/data/2.5/weather?zip=94040,us')
    print('>>>>>>>>>>>>>')

    return dmp_render(request, 'pythonrequest.html',)
