import datetime
from time import sleep


class Generator():

    EPOCH = datetime.datetime(2025, 2, 13, tzinfo = datetime.timezone.utc)
    PRIMES = [3, 5, 7, 11, 13, 17, 19, 23, 29]

    def check(self, value: str) -> bool:
        timestamp = value[:-1]
        pairity = self.pairity(base34_to_int(timestamp))
        if pairity == value[-1]: return True
        
        return False

    def generate(self) -> str:
        """
        Generate a unique identifier based on the current time.
        """
        sleep((100-self.get_tick()%100)/1000)

        timecode = int(self.get_tick()/100)
        pairity = self.pairity(timecode)
        return int_to_base34(timecode) + pairity
    
    def get_tick(self) -> int:
        """
        Get the current time in 100's of microseconds since the epoch.
        """
        return int((datetime.datetime.now(datetime.timezone.utc) - self.EPOCH).total_seconds()*1000)


    def pairity(self, code: int) -> str:
        split_code = [int(i) for i in str(code)]
        pairity = sum([(split_code[i] * self.PRIMES[i]) for i in range(len(split_code))])%34
        return int_to_base34(pairity)



def int_to_base34(millisecond: int) -> str:
    if millisecond < 0:
        raise ValueError("Base36 encoding only supports non-negative integers.")
    
    chars = "0123456789ABCDEFGHJKLMNPQRSTUVWXYZ"
    result = ""
    while millisecond:
        millisecond, r = divmod(millisecond, 34)
        result = chars[r] + result
    return result or "0"

def base34_to_int(string: str) -> int:
    chars = "0123456789ABCDEFGHJKLMNPQRSTUVWXYZ"
    result = 0
    for char in string:
        result = result *34 + chars.index(char)
    return result