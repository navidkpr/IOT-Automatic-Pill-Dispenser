"""
1) removes any previously created cron tasks
2) sets cron task to tun java -jar FaxEmail.jar 10 seconds after python3 update_docs_req
"""


from crontab import CronTab
import os

USER = 'pi'
PATH_TO_PROJ = '/home/pi/Desktop/IOT-Automatic-Pill-Dispenser'


if __name__ == '__main__':
    print('schedule_updater.py - removing past doc-update cron jobs and scheduling json request, then 10 second delay and java email sending')
    cron = CronTab(user=USER)
    cron.remove_all(comment='update_docs')
    job = cron.new(command='java -jar {}/FaxEmail.jar'.format(PATH_TO_PROJ), comment='update_docs')
    job.minute.on(10)
    job.hour.on(0)
    job = cron.new(command='python3 {}/update_doc_req.py'.format(PATH_TO_PROJ), comment='update_docs')
    job.minute.on(0)
    job.hour.on(0)
    cron.write(user=USER)
    os.system('service cron start')

