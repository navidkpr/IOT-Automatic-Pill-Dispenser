from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete, post_init
from django.dispatch import receiver
from schedule.models import Medicine, Container, Client
from schedule.cron_scheduler import create_cron, remove_cron
#def create_cron(name, hour, id_):
    #print("create_cron name: " + name + " id: " + str(id_) + " hour: " + str(hour))


#def remove_cron(id_):
    #print("remove_cron id: " + str(id_))

@receiver(post_save, sender=Client)
def makeContainers(sender, instance, created=False, **kwargs):
    Medicine.objects.filter(user_id=instance.pk).delete()
    Container.objects.filter(user_id=instance.pk).delete() 
    print("HEll")
    for i in range(21):
        try:
            print(instance.pk)
            cont = Container(number=i+1, busy=0, drug_id=-1, user_id=instance.pk)
            print(cont)
            cont.save()
        except Exception as e:
            print(e);

@receiver(pre_delete, sender=Client)
def deleteClientFiles(sender, instance, created=False, **kwargs):
    Medicine.objects.filter(user_id=instance.pk).delete()
    Container.objects.filter(user_id=instance.pk).delete() 
    

@receiver(pre_save, sender=Medicine)
def my_handler2(sender, instance, created=False, **kwargs):
    print("Called pre_save")
        #if instance.container == 0:
            #send error for all slots being full


@receiver(post_save, sender=Medicine)
def my_handler1(sender, instance, created=False, **kwargs):
    print("Called post_save")
    remove_cron(instance.id)
    tray_num = None
    for i in range(20, -1, -1):
        print(instance.user_id)
        print(i)
        try:
            obj = Container.objects.filter(number=i+1).filter(user_id = instance.user_id).first()
            print(obj)
            if obj.busy == 0 or instance.pk == obj.drug_id:
                tray_num = i + 1
                if instance.id == obj.drug_id:
                    break;
        except Exception  as e:
            print(e)

    print(tray_num)
    obj = Container.objects.filter(number=tray_num).filter(user_id=instance.user_id)
    obj.update(busy = 1)
    print('don')
    obj.update(drug_id = instance.pk)
    print("don2")
    try:
        print("tray nubmer is: " + str(obj.first().number))
        instance.container = int(obj.first().number)
        print(instance.container)
    except Exception as e:
        print(e)
    time_gap = instance.timeGap
    startTime = 0
    try:
        while startTime <= 20 and startTime > -2:
            create_cron(instance.name, startTime, instance.id, tray_num, Client.objects.filter(pk = instance.user_id).first().phone)
            startTime += time_gap
    except Exception as e:
        print(e)
####test Container
@receiver(pre_delete, sender=Medicine)
def delete_handler(sender, instance = False, created = False, **kwargs):
    print("instance container is : {}".format(instance.container))
    if instance.container != 0:
        obj = Container.objects.filter(number = instance.container).filter(user_id = instance.user_id)
        obj.update(busy = 0)
        obj.update(drug_id = -1)
    remove_cron(instance.id)
