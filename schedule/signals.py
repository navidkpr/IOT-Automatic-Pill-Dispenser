from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from schedule.models import Medicine
#from cron_scheduler import create_cron, remove_cron

def create_cron(name, hour, id_, containter = False):
    print("create_cron name: " + name + " id: " + str(id_) + " hour: " + str(hour))


def remove_cron(id_):
    print("remove_cron id: " + str(id_))

@receiver(post_save, sender=Medicine)
def my_handler1(sender, instance, created=False, **kwargs):
    if instance._state.adding is False:
        remove_cron(instance.id)
    time_gap = instance.timeGap
    startTime = 0
    while startTime <= 20:
        create_cron(instance.name, startTime, instance.id)
        startTime += time_gap

@receiver(pre_delete, sender=Medicine)
def delete_handler(sender, instance = False, created = False, **kwargs):
    remove_cron(instance.id)
