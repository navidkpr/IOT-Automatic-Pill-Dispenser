from cron_scheduler import create_cron, remove_cron

print('creating cron')
create_cron('hello', -1, '22', 7)
