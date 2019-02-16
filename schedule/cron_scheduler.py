from crontab import CronTab
import os


def create_cron(hour: int, id_: str, container: str = 'container'):
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
    print("create_cron id: " + str(id_) + " hour: " + str(hour))
    cron = CronTab()
    job = cron.new(command=f'python {os.getcwd()}/dispense.py {container}', comment=str(id_))
    job.hour.every(hour)


def remove_cron(id_: str):
    """
    - removes a cron job with name <id_>
    """
    print("remove_cron id: " + str(id_))
    cron = CronTab()
    commands = cron.remove_all(comment=str(id_))
