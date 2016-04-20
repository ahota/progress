import sys, time

class ProgressBar:
    def __init__(self, iterations, bar_length):
        self.iterations = iterations
        self.bar_length = bar_length
        self.bookends = '[]'
        self.barchar  = '#'
        self.emptychar= ' '
        self.cur_tick = 0

    def start(self):
        self.start_time = time.time()
        self.print_bar(time.time())

    def finish(self):
        stop_time = time.time()
        td = self.time_diff(self.start_time, stop_time)
        sys.stderr.write('\n{0}\n'.format(td))

    def tick(self):
        self.cur_tick += 1
        self.print_bar(time.time())

    def print_bar(self, cur_time):
        percent = float(self.cur_tick) / self.iterations
        bar = self.barchar * int(round(percent * self.bar_length))
        empty = self.emptychar * (self.bar_length - len(bar))
        pb_string = '\r{0}{1}{2} {3}%, {4} it. '.format(
                self.bookends[0], bar+empty, self.bookends[1],
                int(round(percent*100)), self.cur_tick)
        td = self.time_diff(self.start_time, cur_time)
        sys.stderr.write(pb_string + td + ' '*(80 - len(pb_string) - len(td)))
        sys.stderr.flush()

    def time_diff(self, s, e):
        output = 'Elapsed time: '
        diff = int(e - s)
        if diff > 3600:
            hours = diff / 3600
            diff = diff % 3600
            output += str(hours) + 'h, '
        if diff > 60:
            minutes = diff / 60
            diff = diff % 60
            output += str(minutes) + 'm, and '
        output += str(diff) + 's'
        return output

