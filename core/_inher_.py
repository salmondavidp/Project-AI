import datetime

# A class to return system info.
class SystemInfo:
    def _inher_(self):
        pass
    
    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = 'The time now is {} {}'.format(now.hour, now.minute)
        return answer