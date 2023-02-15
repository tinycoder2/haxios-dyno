from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Participant(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name", max_length=200, blank=False, null=False)
    phone = models.CharField(verbose_name="Contact Number",max_length=10, null=False, blank=False, )
    insta = models.CharField(verbose_name="Instagram ID", max_length=200, blank=False, null=False)
    score = models.IntegerField(default=0)

