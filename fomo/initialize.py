from datetime import datetime
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'fomo.settings'
import django
django.setup()

from django.core import management
from django.db import connection
from django.contrib.auth.models import Permission, Group



# initialize the django environment


# for p in Permission.objects.all():
#     print(p.codename, '> ', p.name)

#This will drop the database and migrate

# ensure the user really wants to do this
areyousure = input('''
  You are about to drop and recreate the entire database.
  All data are about to be deleted.  Use of this script
  may cause itching, vertigo, dizziness, tingling in
  extremities, loss of balance or coordination, slurred
  speech, temporary zoobie syndrome, longer lines at the
  testing center, changed passwords in Learning Suite, or
  uncertainty about whether to call your professor
  'Brother' or 'Doctor'.

  Please type 'yes' to confirm the data destruction: ''')
if areyousure.lower() != 'yes':
    print()
    print('  Wise choice.')
    sys.exit(1)

# initialize the django environment
os.environ['DJANGO_SETTINGS_MODULE'] = 'fomo.settings'
import django
django.setup()


# drop and recreate the database tables
print()
print('Living on the edge!  Dropping the current database tables.')
with connection.cursor() as cursor:
    cursor.execute("DROP SCHEMA public CASCADE")
    cursor.execute("CREATE SCHEMA public")
    cursor.execute("GRANT ALL ON SCHEMA public TO postgres")
    cursor.execute("GRANT ALL ON SCHEMA public TO public")
# make the migrations and migrate
management.call_command('makemigrations')
management.call_command('migrate')

from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType

from decimal import Decimal
from datetime import datetime
from account.models import FomoUser
from catalog import models as cmod

#End of database drop and migrations


#PERMISSION CREATION
content_type =ContentType.objects.get_for_model(FomoUser)
permissions = Permission.objects.create(
    codename = 'View_products',
    name = 'Can view list of products',
    content_type = content_type,
    )

permissions = Permission.objects.create(
    codename = 'View_users',
    name = 'Can view list of users',
    content_type = content_type,
    )

#GROUPS CREATION
g1 = Group()
g1.name = 'Manager'
g1.save()

g2 = Group()
g2.name = 'Salesperson'
g2.save()

g3 = Group()
g3.name = 'Admin'
g3.save()

'Permissions creation'

g1.permissions.add(Permission.objects.get(codename=('add_fomouser')))
g1.permissions.add(Permission.objects.get(codename=('change_fomouser')))
g1.permissions.add(Permission.objects.get(codename=('add_product')))
g1.permissions.add(Permission.objects.get(codename=('change_product')))
g1.permissions.add(Permission.objects.get(codename=('View_products')))
g1.permissions.add(Permission.objects.get(codename=('View_users')))


g2.permissions.add(Permission.objects.get(codename=('View_products')))
g2.permissions.add(Permission.objects.get(codename=('View_users')))


for p in Permission.objects.all():
    # print(p.code)
    g3.permissions.add(p)
g3.permissions.add(Permission.objects.get(codename=('View_products')))
g3.permissions.add(Permission.objects.get(codename=('View_users')))
g3.permissions.add(Permission.objects.get(codename=('change_fomouser')))







#Query all / some with different query OPTIONS
# 3 - 5 examples

u1 = FomoUser()
u1.first_name = "Stephane"
u1.last_name = "Akoki"
u1.username = "Akokixav"
u1.set_password("jeuvideo")
u1.address = "Provo"
u1.zip = '84604'
u1.date_joined = datetime.now()
u1.last_login = datetime.now()
u1.email = "akokistephane@gmail.com"
u1.phone_number = "8013863392"
u1.city ="Provo"
u1.state = "UT"
u1.is_staff = True
u1.is_active = True
u1.save()



u2 = FomoUser()
u2.first_name = "Xavier"
u2.last_name = "Akoki"
u2.username = "Xav1"
u2.set_password("jeuvideo")
u2.address = "Draper"
u2.zip = '84604'
u2.date_joined = datetime.now()
u2.last_login = datetime.now()
u2.email = "xavier1@gmail.com"
u2.phone_number = "8013863392"
u2.city ="Provo"
u2.state = "UT"
u2.is_staff = True
u2.is_active = True
u2.save()

u3 = FomoUser()
u3.first_name = "Yapi"
u3.last_name = "Akoki"
u3.username = "yapi1"
u3.set_password("jeuvideo")
u3.address = "Draper"
u3.zip = '84604'
u3.date_joined = datetime.now()
u3.last_login = datetime.now()
u3.email = "yapi2@gmail.com"
u3.phone_number = "8013863392"
u3.city ="Orem"
u3.state = "UT"
u3.is_staff = True
u3.is_active = True
u3.save()

#Adding user to group
gadmin = Group.objects.get(name='Admin')
gadmin.user_set.add(u1)

gmanager = Group.objects.get(name='Manager')
gmanager.user_set.add(u2)

gsales = Group.objects.get(name='Salesperson')
gsales.user_set.add(u3)

print('>>>>>>>>>>>>>>>>')
u1 = FomoUser.objects.get(id=1)
print(u1.username)

# mygrouplist = FomoUser.objects.filter(groups_name = 'Admin')
# print(mygrouplist)





#categories
cat1 = cmod.Category();
cat1.code = 'brass'
cat1.name = 'Brass Instruments'
cat1.save()

cat2 = cmod.Category();
cat2.code = 'woodwind'
cat2.name = 'Woodwind Instruments'
cat2.save()

cat3 = cmod.Category();
cat3.code = 'string'
cat3.name = 'String Instruments'
cat3.save()
#end of category creation



#Bulk Products
bp1 = cmod.BulkProduct();
bp1.category = cat3
bp1.name = 'Guitar Strings'
bp1.brand = 'Gibson'
bp1.price = Decimal('15.50')
bp1.quantity = 40
bp1.reorder_trigger = 10
bp1.reorder_quantity = 30
bp1.serial_number = 'jopih78'
bp1.save()

bp2 = cmod.BulkProduct();
bp2.category = cat1
bp2.name = 'Trumpet Mouthpiece'
bp2.brand = 'Yamaha'
bp2.price = Decimal('25.00')
bp2.quantity = 30
bp2.reorder_trigger = 10
bp2.reorder_quantity = 20
bp2.serial_number = 'ijnh09'
bp2.save()
#end of bulk products


#UniqueProduct
up1 = cmod.UniqueProduct();
up1.category = cat1 #
up1.name = 'Trumpet' #
up1.brand = 'Yamaha' #
up1.price = Decimal('899.99') #
up1.serial_number = '747amfhuefhi' #
# up1.ProductPictures = '${STATIC_URL}catalog/media/violin.png'
up1.save() #

up2 = cmod.UniqueProduct();
up2.category = cat2 #
up2.name = 'Saxophone' #
up2.brand = 'Selmer' #
up2.price = Decimal('750.00') #
up2.serial_number = '897dnsaiuefhi' #
up2.save()

up3 = cmod.UniqueProduct();
up3.category = cat2 #
up3.name = 'Saxophone' #
up3.brand = 'Selmer' #
up3.price = Decimal('750.00') #
up3.serial_number = '897dnsaiuefhi' #
up3.save()

up4 = cmod.UniqueProduct();
up4.category = cat3 #
up4.name = 'Violin' #
up4.brand = 'Bella' #
up4.price = Decimal('750.00') #
up4.serial_number = '897dnsaiuefhi' #
up4.save()

up5 = cmod.UniqueProduct();
up5.category = cat2 #
up5.name = 'Piano' #
up5.brand = 'Kawai' #
up5.price = Decimal('750.00') #
up5.serial_number = '897dnsaiuefhi' #
up5.save()

#end of unique products




#VIOLIN PICTURES
pic = cmod.ProductPictures();
pic.subdir ='violin.png'
pic.alttext = "This is a violin"
pic.minetype = "png"
pic.product = up4;
pic.save()

pic = cmod.ProductPictures();
pic.subdir ='violin2.png'
pic.alttext = "This is a violin"
pic.minetype = "png"
pic.product = up4;
pic.save()

pic = cmod.ProductPictures();
pic.subdir ='violin3.png'
pic.alttext = "This is a violin"
pic.minetype = "png"
pic.product = up4;
pic.save()


#SAXOPHONE PICTURES
pic = cmod.ProductPictures();
pic.subdir ='Saxophone.png'
pic.alttext = "This is a saxo"
pic.minetype = "png"
pic.product = up3;
pic.save()

pic = cmod.ProductPictures();
pic.subdir ='Saxophone.png'
pic.alttext = "This is a saxo"
pic.minetype = "png"
pic.product = up2;
pic.save()

pic = cmod.ProductPictures();
pic.subdir ='piano.png'
pic.alttext = "This is a piano"
pic.minetype = "png"
pic.product = up5;
pic.save()

pic = cmod.ProductPictures();
pic.subdir ='guitarstrings.png'
pic.alttext = "Guitar Strings"
pic.minetype = "png"
pic.product = bp1;
pic.save()

pic = cmod.ProductPictures();
pic.subdir ='trumpetmp.png'
pic.alttext = "mouth piece"
pic.minetype = "png"
pic.product = bp2;
pic.save()

pic = cmod.ProductPictures();
pic.subdir ='trumpet.png'
pic.alttext = "trumpet"
pic.minetype = "png"
pic.product = up1;
pic.save()

pic = cmod.ProductPictures();
pic.subdir ='trumpet.png'
pic.alttext = "trumpet"
pic.minetype = "png"
pic.product = up2;
pic.save()
