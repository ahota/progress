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

Running `main.py` will show a few working examples with user-customizable features
