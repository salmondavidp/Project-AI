import datetime

# A class to return system info.
class SystemInfo:
    def __init__(self):
        pass
    
    @staticmethod
    def get_date():
        now = datetime.datetime.now()
        answer = 'The date is {} {} {}'.format( now.day,now.month, now.year)
        return answer
    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = 'The time is {} {}'.format( now.minute, now.hour, now.second)
        return answer
      
  