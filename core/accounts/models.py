from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    age = models.IntegerField()
    email_address = models.EmailField()
    name = models.CharField(max_length=255)
    national_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address
        self.save()

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age
        self.save()

    def get_email(self):
        return self.email_address

    def set_email(self, email_address):
        self.email_address = email_address
        self.save()

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        self.save()

    def get_national_code(self):
        return self.national_code

    def set_national_code(self, national_code):
        self.national_code = national_code
        self.save()

    def get_phone(self):
        return self.phone_number

    def set_phone(self, phone_number):
        self.phone_number = phone_number
        self.save()


class Wallet(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='wallet')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.profile.user.username}'s Wallet"

# Signal to create Wallet when Profile is created
@receiver(post_save, sender=Profile)
def create_or_update_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(profile=instance)
    instance.wallet.save()
