from django.db import models

# Create your models here.


class mainnews(models.Model):
    news1 = models.CharField(max_length=200)
    subnews1 = models.TextField(max_length=100000)
    image1 = models.ImageField(upload_to='news/images')
    date1 = models.DateField(blank=False, null=True)
    news2 = models.CharField(max_length=200,)
    subnews2 = models.TextField(max_length=100000)
    image2 = models.ImageField(upload_to='news/images')
    date2 = models.DateField(blank=False, null=True)
    news3 = models.CharField(max_length=200)
    subnews3 = models.TextField(max_length=100000)
    image3 = models.ImageField(upload_to='news/images')
    date3 = models.DateField(blank=False, null=True)
    news4 = models.CharField(max_length=200)
    subnews4 = models.TextField(max_length=100000)
    image4 = models.ImageField(upload_to='news/images')
    date4 = models.DateField(blank=False, null=True)
    news5 = models.CharField(max_length=200)
    subnews5 = models.TextField(max_length=100000)
    image5 = models.ImageField(upload_to='news/images')
    date5 = models.DateField(blank=False, null=True)
    news6 = models.CharField(max_length=200)
    subnews6 = models.TextField(max_length=100000)
    image6 = models.ImageField(upload_to='news/images')
    date6 = models.DateField(blank=False, null=True)

    news7 = models.CharField(max_length=200)
    subnews7 = models.TextField(max_length=100000)
    image7 = models.ImageField(upload_to='news/images')
    date7 = models.DateField(blank=False, null=True)
    news8 = models.CharField(max_length=200)
    subnews8 = models.TextField(max_length=100000,)
    image8 = models.ImageField(upload_to='news/images')
    date8 = models.DateField(blank=True, null=True)
