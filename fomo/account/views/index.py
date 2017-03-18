from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
import random
from account import models as amod


@view_function
def process_request(request):

    user = amod.FomoUser.objects.get(id = request.user.id)

    context = {
        'user': user
    }


    return dmp_render(request, 'index.html', context)
