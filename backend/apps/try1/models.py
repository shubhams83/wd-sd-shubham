from email.mime import image
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Try1(models.Model):
    class Meta(object):
        db_table = 'try'

    image = CloudinaryField(
        'Image', null= True, blank= False
    )