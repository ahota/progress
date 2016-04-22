from progress import ProgressBar
from time import sleep
from random import random

my_list = range(20)

print 'TEST: Using a default ProgressBar'
sleep(1.0)
pb = ProgressBar(len(my_list), 20)
pb.start()
for i in my_list:
    sleep(0.3)
    pb.tick()
pb.finish()

print 'TEST: Using a custom design'
sleep(1.0)
pb = ProgressBar(len(my_list), 20, bookends='<{}>', 
        bar_char='/', empty_char='-')
pb.start()
for i in my_list:
    sleep(0.3)
    pb.tick()
pb.finish()

print 'TEST: Using a minimal design'
sleep(1.0)
pb = ProgressBar(len(my_list), 20, bookends='', 
        bar_char='-', empty_char=' ', show_percent=True, show_iter=False,
        show_time=False)
pb.start()
for i in my_list:
    sleep(0.3)
    pb.tick()
pb.finish()

print 'TEST: Using a named job'
sleep(1.0)
pb = ProgressBar(len(my_list), 20, job_name='Test Job')
pb.start()
for i in my_list:
    sleep(0.3)
    pb.tick()
pb.finish()

print 'TEST: Using a bar with ETA'
sleep(1.0)
pb = ProgressBar(len(my_list), 20, show_eta=True)
pb.start()
for i in my_list:
    sleep(0.5)
    pb.tick()
pb.finish()

