from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'

class Brand(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name='brands', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    eighth_price = models.IntegerField(blank=True, null=True)
    quarter_price = models.IntegerField(blank=True, null=True)
    half_price = models.IntegerField(blank=True, null=True)
    ounce_price = models.IntegerField(blank=True, null=True)
    kind = models.CharField(max_length=50)
    tac = models.FloatField(blank=True, null=True)
    thc = models.FloatField(blank=True, null=True)
    cbd = models.FloatField(blank=True, null=True)
    slug = models.SlugField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
