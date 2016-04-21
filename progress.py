import sys, time

class ProgressBar:
    def __init__(self, iterations, bar_length, bookends='[]', bar_char='#',
            empty_char=' ', show_percent=True, show_iter=True, show_time=True,
            term_width=80, job_name=''):
        self.iterations   = iterations
        self.bar_length   = bar_length
        self.begin_char   = bookends[0:len(bookends)/2]
        self.end_char     = bookends[len(bookends)/2: ]
        self.bar_char     = bar_char
        self.empty_char   = empty_char
        self.show_percent = show_percent
        self.show_iter    = show_iter
        self.show_time    = show_time
        self.term_width   = term_width
        self.job_name     = job_name

    def start(self):
        self.cur_tick = 0
        self.start_time = time.time()
        self.print_bar(time.time())

    def finish(self):
        prefix = 'Total time'
        prefix += ' for '+self.job_name+': ' if self.job_name != '' else ': '
        td = prefix + self.time_diff(self.start_time, time.time())
        sys.stderr.write('\n{0}\n'.format(td))

    def tick(self):
        self.cur_tick += 1
        self.print_bar(time.time())

    def print_bar(self, cur_time):
        pb = self.build_bar()
        td = 'Elapsed time: ' + self.time_diff(self.start_time, cur_time) \
                if self.show_time else ''
        sys.stderr.write(pb + td + ' '*(self.term_width - len(pb) - len(td)))
        sys.stderr.flush()

    def time_diff(self, s, e):
        output = ''
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

    def build_bar(self):
        percent = float(self.cur_tick) / self.iterations
        bar = self.bar_char * int(round(percent * self.bar_length))
        empty = self.empty_char * (self.bar_length - len(bar))
        pb_string = '\r{0}{1}{2} {3}%{4}'.format(
                self.begin_char, bar+empty, self.end_char,
                int(round(percent*100)) if self.show_percent else '',
                ', '+str(self.cur_tick)+' it. ' if self.show_iter else '')
        return pb_string
