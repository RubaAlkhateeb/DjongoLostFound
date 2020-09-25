from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from datetime import datetime, date


class Post(models.Model):
    Item_Name = models.CharField(max_length=255, null=False)
    Founder = models.CharField(max_length=255)
    Contect_Information = models.CharField(max_length=255, null=False)
    Date = models.DateField()
    Description = models.TextField()
    Image = models.ImageField(null=True, blank=True, upload_to ='uploads/')

    def __str__(self):
        return self.Item_Name + ' | ' + self.Founder

    def get_absolute_url(self):
        return reverse('ItemDetail', args=(str(self.id)))