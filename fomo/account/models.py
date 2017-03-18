from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Define models here

#INHERITENCE PATH

    # AbstractBaseUser
    #     |
    #     |
    #
    # AbstractUser
    #     |
    #     |
    # USER



#
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)


# # CONTACT_CHOICES = [
# #     ['text', 'Text']
# #     ['email', 'Email']
# #     ['voice', 'Voice']
#
#
#
# ]
class FomoUser(AbstractUser):
	# inherits from AbstractBaseUser:
	## password
	## last_login

	# inherits from PermissionsMixIn
	## is_superuser
	## groups
	## user_permissions

	# inherits from AbstractUser:
	## username_validator
	## username
	## first_name
	## last_name
	## email
	## is_staff
	## is_active
	## date_joined

    phone_number = models.CharField(max_length = 20)
    address = models.TextField()
    city = models.TextField()
    state = models.CharField(max_length = 2)
    zip = models.IntegerField()


    # def get_age(self):
    #     #u1 variable doesn't exist, but the object does , because we are inside of the objects
    #     return datetime.datetime.now() -self birthdate
