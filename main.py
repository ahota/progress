from progress import ProgressBar
from time import sleep

my_list = range(20)
pb = ProgressBar(len(my_list), 20)
pb.start()
for i in my_list:
    sleep(0.5)
    pb.tick()
pb.finish()
