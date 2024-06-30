from django.db import models
from django.urls import reverse


# Create your models here.
class Company(models.Model):
    companyname = models.CharField(max_length=128)
    ceo = models.CharField(max_length=64)
    headquarters = models.CharField(max_length=64)
    foundedyear = models.IntegerField()
    typeofcompany = models.CharField(max_length=64)
    primaryindustry = models.CharField(max_length=64)

    def __str__(self):
        return self.companyname

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})
