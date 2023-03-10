from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import CustomUser


@receiver(post_save, sender=CustomUser)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            "Welcome Goodreads",
            f"Hi {instance.username} welcome goodreads clone",
            "fzliddinbahromov9717@gmail.com",
            [instance.email],
            fail_silently=False
        )