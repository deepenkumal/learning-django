from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

@receiver(post_save,sender = User)
def build_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user = instance)

#post_save.connect(build_profile ,sender = User)
