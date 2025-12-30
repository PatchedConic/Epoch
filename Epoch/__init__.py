import datetime
from time import sleep

INTERVAL = .1  # seconds

class Generator():

    EPOCH = datetime.datetime(2025, 2, 13, tzinfo = datetime.timezone.utc)
    PRIMES = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]

    def check(self, value: str) -> bool:
        timestamp = value[:-1]
        pairity = self.pairity(base34_to_int(timestamp))
        if pairity == value[-1]: return True
        
        return False

    def generate(self, n:int = 1) -> str:
        """
        Generate a unique identifier based on the current time.
        Args:
            n (int): number of ID's to return. 
        """
        identifiers = []

        for i in range(n):
            sleep((INTERVAL-(self.get_tick()%INTERVAL)))
            timecode = int(self.get_tick()/INTERVAL)
            pairity = self.pairity(timecode)
            value = int_to_base34(timecode) + pairity
            if self.check(value) == False:
                raise Exception("Generator pairity check failed")
            identifiers.append(value)
        return tuple(identifiers)
 
    def get_tick(self) -> float:
        """
        Get the current time in seconds since the epoch.
        """
        return round((datetime.datetime.now(datetime.timezone.utc) - self.EPOCH).total_seconds(), 3)


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