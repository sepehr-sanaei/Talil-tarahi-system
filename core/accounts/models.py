from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

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
