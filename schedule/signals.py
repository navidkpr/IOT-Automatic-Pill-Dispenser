from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from schedule.models import Medicine, Container
from schedule.cron_scheduler import create_cron, remove_cron
#def create_cron(name, hour, id_):
    #print("create_cron name: " + name + " id: " + str(id_) + " hour: " + str(hour))


#def remove_cron(id_):
    #print("remove_cron id: " + str(id_))

@receiver(pre_save, sender=Medicine)
def my_handler2(sender, instance, created=False, **kwargs):
    print("Called pre_save")
    if instance.container == 0:
        for i in range(21):
            print(i)
            obj = Container.objects.filter(number=i + 1)
            if obj.values_list('busy', flat=True)[0] == 0:
                print("went into if")
                obj.update(busy = 1)
                obj.update(drug_id = instance.id)
                instance.container = i+1
                break;
        #if instance.container == 0:
            #send error for all slots being full


@receiver(post_save, sender=Medicine)
def my_handler1(sender, instance, created=False, **kwargs):
    print("Called post_save")
    remove_cron(instance.id)
    print("checking")
    time_gap = instance.timeGap
    startTime = 0
    while startTime <= 20 and startTime > -2:
        create_cron(instance.name, startTime, instance.id, instance.container)
        startTime += time_gap
####test Container
@receiver(pre_delete, sender=Medicine)
def delete_handler(sender, instance = False, created = False, **kwargs):
    print("instance container is : {}".format(instance.container))
    if instance.container != 0:
        obj = Container.objects.filter(number = instance.container)
        obj.update(busy = 0)
        obj.update(drug_id = -1)
    remove_cron(instance.id)
