import datetime
from multiprocessing.connection import answer_challenge
class SysytemInfo:

    def _init(self):
        pass
    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = 'The time is {} {}'.format(now.hour,now.minute)
        return answer
