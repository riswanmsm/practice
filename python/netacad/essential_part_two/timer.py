def two_dig(val):
    if val < 10:
        return '0' + val
    else:
        return val

class Timer:
    '''
    class able to count seconds
    Its constructor accepts three arguments representing 
    hours (a value from the range [0..23]
    minutes (from the range [0..59])
    seconds (from the range [0..59])
    Zero is the default value for all of the above parameters

    objects should be printable as hh:mm:ss with leading zero for appropriate value

    having two methods called next_second() and previous_second() to increment and decrement 1 seconds respectively
    '''
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return two_dig
