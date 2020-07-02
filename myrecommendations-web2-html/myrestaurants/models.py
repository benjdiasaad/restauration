from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    street = models.CharField(max_length=255, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=255, default="")
    zipCode = models.CharField(max_length=255, blank=True, null=True)
    stateOrProvince = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('myrestaurants:restaurant_detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField('Euro amount', max_digits=8, decimal_places=2, blank=True,
        null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateField(default=date.today)
    image = models.ImageField(upload_to="myrestaurants", blank=True, null=True)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.PROTECT, related_name='dishes')

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('myrestaurants:dish_detail', kwargs={'pkr': self.restaurant.pk, 'pk': self.pk})
    def __str__(self):
        return self.name

class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True

class RestaurantReview(Review):
    restaurant = models.ForeignKey('Restaurant',on_delete=models.PROTECT)