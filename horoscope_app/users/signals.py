from django.db.models.signals import post_save, post_init, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from .get_sign import return_sign


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # print(f'post save profile instance: {instance.profile}')
    instance.profile.sign = return_sign(instance.profile.birthday)
    instance.profile.save()



@receiver(pre_save, sender=Profile)
def save_sign(sender, instance, **kwargs):
    sender.sign = return_sign(instance.birthday)