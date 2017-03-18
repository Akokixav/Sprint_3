from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
import random
from account import models as amod


@view_function
# @login_required
def process_request(request):
    context = {

    }


    return dmp_render(request, 'index.html', context)
