class TimeInterval:

    # A utility method
    from_secs = lambda s: (s // 3_600, s // 60 % 60, s % 60)

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.secs = 3_600 * hours + 60 * minutes + seconds
        # self.hours, self.minutes, self.seconds = TimeInterval.from_secs(self.secs)
    
    def __add_sub(self, other, op=1):
        """ The last argument is 1 for addition (default), and -1 for
        subtraction
        """
        if isinstance(other, int):
            other = TimeInterval(seconds=other)
        
        if isinstance(other, TimeInterval):
            return TimeInterval(seconds=abs(self.secs + op * other.secs))
        
        raise TypeError

    def __add__(self, other):
        return self.__add_sub(other)
    
    def __sub__(self, other):
        return self.__add_sub(other, -1)
    
    def __mul__(self, other):
        if isinstance(other, int):
            return TimeInterval(seconds=self.secs * other)
        raise TypeError

    def __str__(self):
        hours, minutes, seconds = TimeInterval.from_secs(self.secs)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

fti, sti = TimeInterval(21, 58, 50), TimeInterval(1, 45, 22)

assert str(fti + sti) == '23:44:12'
assert str(fti - sti) == '20:13:28'
assert str(fti * 2) == '43:57:40'

assert str(fti + 62) == '21:59:52'
assert str(fti - 62) == '21:57:48'