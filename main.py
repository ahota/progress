from progress import ProgressBar
from time import sleep

my_list = range(20)

print 'TEST: Using a default ProgressBar'
sleep(1.0)
pb = ProgressBar(len(my_list), 20)
pb.start()
for i in my_list:
    sleep(0.1)
    pb.tick()
pb.finish()

print 'TEST: Using a custom design'
sleep(1.0)
pb = ProgressBar(len(my_list), 20, bookends='<||>', 
        bar_char='/', empty_char='-')
pb.start()
for i in my_list:
    sleep(i/20.0)
    pb.tick()
pb.finish()
