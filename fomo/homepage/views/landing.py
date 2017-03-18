from django.conf import settings
from django_mako_plus import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_string
import random
from account import models as amod

@view_function
def process_request(request):
    # stephane = amod.FomoUser.objects.filter(first_name = "Stephane")[0]
    context = {
        'now': datetime.now(),
        'timecolor': random.choice(['red', 'blue', 'green', 'red']),
        # 'username': stephanie.first_name
    }
    # users = amod.FomoUser.objects.all() #get all the objects
    # user = amod.FomoUsers.objects.get(id='###') #return only one object


    print('>>>>>>>>>>', context)
    print('>>>>>>>>>>', 'username')
    return dmp_render(request, 'landing.html', context)
