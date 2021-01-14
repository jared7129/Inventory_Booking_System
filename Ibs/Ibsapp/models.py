from django.db import models
from datetime import datetime,date,timedelta
from django.utils import timezone
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.http import HttpResponseRedirect

class Member(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    date_joined=models.DateTimeField(default=timezone.now)
    booking_count=models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    id_no=models.IntegerField(default=101)
    title=models.CharField(max_length=200,default='Item1')
    description=models.CharField(max_length=200)
    remaining_count=models.IntegerField(default=3)
    expiration_date=models.DateTimeField(default=timezone.now)
    # check_out=models.BooleanField(default=False)

    
    def __str__(self):
        return str(self.id_no)

    def __str__(self):
        return str(self.title)


class Booking(models.Model):
    # guest_name=models.CharField(max_length=200)
    inventory=models.ForeignKey(Inventory,on_delete=models.CASCADE)
    member=models.ForeignKey(Member,on_delete=models.CASCADE)
    booking_date=models.DateTimeField(default=timezone.now)
    is_active=models.BooleanField(default=True)

    def clean(self):
        if self.member.booking_count >= 2 and self.is_active == True:
            raise ValidationError('You have reached a maximum of 2 bookings for this member')

        if self.inventory.remaining_count == 0 and self.is_active == True:
            raise ValidationError('There is no more stock of this item')


    def __str__(self):
        return self.member.name
    
@receiver(post_save,sender=Booking)
def  RType(sender, instance, created, **kwargs):
    inventory = instance.inventory
    member = instance.member
    if created:
        inventory.remaining_count = inventory.remaining_count - 1
        member.booking_count += 1
    if instance.is_active == False:
        inventory.remaining_count += 1
        member.booking_count = member.booking_count - 1
    inventory.save()
    member.save()
    member = instance.member
