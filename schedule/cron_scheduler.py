from crontab import CronTab
import os


USER = 'pi'


def create_cron(name: str, hour: int, id_: str):
    """
    - adds a new cron job to run the dispenser script on dow day of the week
      at time time of the day
    - cron job will have comment <id>
    - parameters
        - dow is "SUN"-"MON"
        - hour is int: 0-23
        - number is the number to dispense
        - container is the container to dispense from
    """
    print("cron-scheduler - create_cron id: " + str(id_) + " hour: " + str(hour))
    cron = CronTab(user=USER)
    job = cron.new(command='python3 {}/schedule/dispense.py "{}" "{}"'.format(os.getcwd(), name, str(id_)), comment=str(id_))
    if hour < 0:
        job.minute.every(1)
    else:
        job.hour.on(hour)
    cron.write(user=USER)
    os.system('service cron start')


def remove_cron(id_: str):
    """
    - removes a cron job with name <id_>
    """
    print("cron_scheduler - remove_cron id: " + str(id_))
    cron = CronTab(user=USER)
    commands = cron.remove_all(comment=str(id_))
    cron.write(user=USER)
