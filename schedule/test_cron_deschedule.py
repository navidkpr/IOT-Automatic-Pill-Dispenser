from cron_scheduler import create_cron, remove_cron
import sys

print('creating cron')
remove_cron(sys.argv[1])
