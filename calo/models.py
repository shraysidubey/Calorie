from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    Height = models.FloatField(null=False)
    Weight = models.FloatField(null=False)
    TYPE_SELECT = (('female', 'Female'),('male', 'male'),)
    gender=models.CharField(max_length=11,choices=TYPE_SELECT)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
