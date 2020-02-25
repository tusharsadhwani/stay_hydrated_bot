from datetime import datetime

# hours to message are from 9am to 9pm,
# so hour starts at 9, increments by 3 after every message,
# and rolls back to 9 after 21 (9pm)
class MessageTimer:
    def __init__(self, tz):
        # set default timer to 9am
        self._msg_hour = 9
    
        self.timezone = tz

        curr_time = self.get_current_time()
        # catch up to today's next message hour
        if 9 <= curr_time.hour < 21:
            # increment hour till it's greater than current time
            while self.msg_hour < curr_time.hour:
                self.increment()
            print('Next message at hour', self.msg_hour)
    
    @property
    def msg_hour(self):
        return self._msg_hour

    @msg_hour.setter
    def msg_hour(self, value):
        if value % 3 != 0:
            raise ValueError('Hours need to be incremented by multiples of 3')
        
        if not 0 <= value <= 23:
            raise ValueError('Hours need to in range(24)')
        
        self._msg_hour = value  

    def get_current_time(self):
        return datetime.now(tz=self.timezone)

    def increment(self):
        if self.msg_hour + 3 > 21:
            self.msg_hour = 9
        else:
            self.msg_hour += 3
