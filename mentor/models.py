from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    ACTIVE_MODE = (
        ('Mentor', 'Mentor'),
        ('Mentee', 'Mentee'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    active_mode = models.CharField(max_length=6, choices=ACTIVE_MODE, default='Mentee')

    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    twitter =  models.CharField(max_length=100, blank=True)
    github =  models.CharField(max_length=100, blank=True)
    linkedin =  models.CharField(max_length=100, blank=True)
    google =  models.CharField(max_length=100, blank=True)
    mentor = models.BooleanField(default=False)
    interest_in_technology = models.BooleanField(default=False)
    interest_in_marketing = models.BooleanField(default=False)
    interest_in_legal = models.BooleanField(default=False)
    interest_in_leadership = models.BooleanField(default=False)
    interest_in_business = models.BooleanField(default=False)
    interest_in_operations = models.BooleanField(default=False)
    interest_in_investments = models.BooleanField(default=False)
    interest_in_professional_development = models.BooleanField(default=False)

    mentee = models.BooleanField(default=False)
    learn_technology = models.BooleanField(default=False)
    learn_marketing = models.BooleanField(default=False)
    learn_legal = models.BooleanField(default=False)
    learn_leadership = models.BooleanField(default=False)
    learn_business = models.BooleanField(default=False)
    learn_operations = models.BooleanField(default=False)
    learn_investments = models.BooleanField(default=False)
    learn_professional_development = models.BooleanField(default=False)
    ranking = models.IntegerField(blank=True, default='0')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print "create"
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    print "update"
#    if created:
#        Profile.objects.create(user=instance)
    instance.profile.save()


class Datos(models.Model):
    phone = models.CharField(max_length=20, blank=True, default=None)
    facebook = models.CharField(max_length=20, blank=True, default=None)
    location = models.CharField(max_length=20, blank=True, default=None)
    mentor = models.CharField(max_length=20, blank=True, default=None)
    mentee = models.CharField(max_length=20, blank=True, default=None)

'''
class User1(AbstractUser):
    COUNTRIES = ('Mexico','Canada', 'USA')   # Contents are left as an exercise to the reader

    # Address
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50, choices=COUNTRIES)

    # Contact
    mobile = models.CharField(max_length=32)
    home = models.CharField(max_length=32)
    office = models.CharField(max_lenghth=32)
    twitter = models.CharField(max_length=100)

    def __unicode__(self):
        return self.username

'''


class Meeting(models.Model):

    MEETING_STATUS = (
        ('C', 'Canceled'),
        ('S', 'Scheduled'),
        ('D', 'Done'),
        ('I', 'In Process'),
        ('O', 'On Hold')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mentor_name = models.CharField(max_length=100, blank=True)
    mentee_name = models.CharField(max_length=100, blank=True)
    date = models.DateField(null=True, blank=True)
    subject = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=1, choices=MEETING_STATUS)
    comments = models.TextField(max_length=500, blank=True)

