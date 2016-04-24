import sys, time

class ProgressBar:
    """Python progress bar for those long for loops
    
    Note: The progress bar and stats print to stderr and use carriage returns
        to update. Printing to stdout inside your loop is less than ideal.
    """

    def __init__(self, iterations, bar_length, bookends='[]', bar_char='#',
            empty_char=' ', show_percent=True, show_iter=True, show_time=True,
            term_width=80, job_name='', show_eta=False):
        """Create a new ProgressBar object

        Arguments:
            iterations (int): The number of loop iterations this progress bar
                will be tracking. This is usually the length of a list being
                iterated.
            bar_length (int): How many characters long the bar should be. This
                does not include the bookend character(s) length.

        Keyword Arguments:
            bookends (string): Default is '[]'. The characters that enclose the 
                progress bar. The characters in the first half are used for the 
                left bookend, the second half for the right.
            bar_char (char): Default is '#'. The character used for the bar 
                itself. This should be one character.
            empty_char (char): Default is ' '. The character used for the empty
                space in the bar. This should be one character.
            job_name (string): Default is ''. A name for this job. Useful if
                there will be several loops. Each ProgressBar will print the
                time taken for the job upon calling finish()
            term_width (int): Default is 80. The total width for the terminal.
            show_percent (bool): Default is True. Whether to show percentage by
                the bar or not.
            show_iter (bool): Default is True. Whether to show the current
                iteration of the loop or not.
            show_time (bool): Default is True. Wether to show the elapsed time
                or not.
            show_eta (bool): Default is False. Whether to show the estimated
                time remaining or not. Note that this overrides printing the
                elapsed time if set to True.
        """
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
        self.show_eta     = show_eta

    def start(self):
        """Tell the ProgressBar when to the loop is about to begin"""
        self.cur_tick = 0
        self.start_time = time.time()
        if self.job_name != '':
            print 'Starting', self.job_name
        self._print_bar(time.time())

    def finish(self):
        """Tell the ProgressBar when the loop is done and print time taken"""
        prefix = 'Total time'
        prefix += ' for '+self.job_name+': ' if self.job_name != '' else ': '
        td = prefix + self._time_diff(self.start_time, time.time())
        sys.stderr.write('\n{0}\n'.format(td))

    def tick(self):
        """Tell the ProgressBar that one loop iteration has passed"""
        self.cur_tick += 1
        self._print_bar(time.time())

    def _print_bar(self, cur_time):
        pb = self._build_bar()
        td = ''
        if self.show_eta and self.cur_tick > 0:
            td += 'ETA: ' + self._calc_eta(cur_time)
        else:
            td += 'Elapsed time: '+self._time_diff(self.start_time,cur_time) \
                                   if self.show_time else ''
        sys.stderr.write(pb + td + ' '*(self.term_width - len(pb) - len(td)))
        sys.stderr.flush()

    def _time_diff(self, s, e):
        diff = int(e - s)
        return self._get_time_string(diff)

    def _calc_eta(self, c):
        time_spent = c - self.start_time
        iter_left  = self.iterations - self.cur_tick
        return self._get_time_string(int(iter_left * time_spent/self.cur_tick))

    def _get_time_string(self, seconds):
        output = ''
        if seconds > 3600:
            hours = seconds / 3600
            seconds = seconds % 3600
            output += str(hours) + 'h, '
        if seconds > 60:
            minutes = seconds / 60
            seconds = seconds % 60
            output += str(minutes) + 'm, and '
        output += str(seconds) + 's'
        return output

    def _build_bar(self):
        percent = float(self.cur_tick) / self.iterations
        bar = self.bar_char * int(round(percent * self.bar_length))
        empty = self.empty_char * (self.bar_length - len(bar))
        pb_string = '\r{0}{1}{2} {3}%{4}'.format(
                self.begin_char, bar+empty, self.end_char,
                int(round(percent*100)) if self.show_percent else '',
                ', '+str(self.cur_tick)+' it. ' if self.show_iter else '')
        return pb_string
