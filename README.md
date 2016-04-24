#Progress

Python progress bar for those long `for` loops.
It's designed to be fairly simple to use:

```python
from progress import ProgressBar
pb = ProgressBar(len(my_list), 20)
pb.start()
for i in my_list:
    # do work
    pb.tick()
pb.finish()
```

Output of the above looks like this:
```
[#####               ] 25%, 36 it. Elapsed time: 29s
```

Or cutomize it:

```python
pb = ProgressBar(len(my_list), 20, bookends='(||)', bar_char='/',
                 job_name='Parse data', show_eta=True, show_iter=False)
pb.start()
for i in my_list:
    #do work
    pb.tick()
pb.finish()
```

Which looks like this:
```
Starting Parse data
(|///////             |) 35% ETA: 39s
```

Running `main.py` will show a few working examples with user-customizable features
