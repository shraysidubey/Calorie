from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    Height = models.FloatField(null=False)
    Weight = models.FloatField(null=False)
    TYPE_SELECT = (('female', 'Female'),('male', 'male'),)
    gender=models.CharField(max_length=11,choices=TYPE_SELECT)
    age=models.IntegerField(max_length=120,null=False)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class Food_qty(models.Model):
    user = models.ForeignKey(UserProfile)
    food_consume = models.CharField(max_length=200)
    calories = models.FloatField(null=False)
    date_added = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.food_consume

class Activity(models.Model):
    user = models.ForeignKey(UserProfile)
    exercise = models.TextField(max_length=200)
    calories_burned = models.FloatField(null=True)
    date_added = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.exercise


