# from django.core.signals import pre_save
from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.dispatch import receiver
from schedule.models import Medicine
from cron_scheduler import create_cron, remove_cron


@receiver(post_save, sender=Medicine)
def my_handler1(sender, instance, created=False, **kwargs):
    if instance._state.adding is False:
        # Updating existing instance
        remove_cron(instance.id)

    time_gap = instance.timeGap
    startTime = 0
    while startTime <= 20:
        create_cron(startTime, instance.id)
        startTime += time_gap
