from django.db import models

class users(models.Model): #Our user model that saves from name and image field
    Name = models.CharField(max_length=100,db_column='Name',blank=True)
    img = models.ImageField(upload_to = 'pictures',db_column='img',blank=True)
