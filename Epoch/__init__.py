import datetime
from time import sleep

BASE_34_ALPHABET = "0123456789ABCDEFGHJKLMNPQRSTUVWXYZ"
EPOCH = datetime.datetime(2025, 2, 13, tzinfo = datetime.timezone.utc)
PRIMES = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]

class Generator():

    FIXED_LENGTH = None
    PREFIX = None

    def check(self, value: str) -> bool:
        timestamp = value[:-1]
        check_digit = self.check_digit(base34_to_int(timestamp))
        if check_digit == value[-1]: return True
        return False

    def generate(self, n:int = 1) -> str:
        """
        Generate a unique identifier based on the current time.
        Args:
            n (int): number of ID's to return. 
        """
        identifiers = []

        for i in range(n):
            sleep((10-self.get_tick()%10)/1000)
            timecode = int(self.get_tick()/10)
            # value = int_to_base34(timecode) + self.check_digit(timecode)
            # value = int_to_base34(timecode).zfill(Generator.FIXED_LENGTH-1) if 
            #          Generator.FIXED_LENGTH else int_to_base34(timecode)
            if Generator.FIXED_LENGTH:
                value = int_to_base34(timecode).zfill(Generator.FIXED_LENGTH-1)
            else:
                value = int_to_base34(timecode)
            check = self.check_digit(value)
            code = value + check
            print(code)
            if self.check(code) == False:
                raise Exception("Generator check_digit check failed")
            identifiers.append(code)
        return tuple(identifiers)
 
    def get_tick(self) -> int:
        """
        Get the current time in 100's of microseconds since the epoch.
        """
        return int((datetime.datetime.now(datetime.timezone.utc) - EPOCH).total_seconds()*1000)


    def check_digit(self, code: str) -> str:
        total = 0
        split_code = [str(i) for i in str(code)]
        for i in range(len(split_code)):
            index = BASE_34_ALPHABET.find(split_code[i])
            if index == -1:
                raise ValueError(f"Invalid character {split_code[i]} in code.")
            total += index * PRIMES[i]
        return int_to_base34(total % 34)



def int_to_base34(millisecond: int) -> str:
    if millisecond < 0:
        raise ValueError("Base36 encoding only supports non-negative integers.")
    result = ""
    while millisecond:
        millisecond, r = divmod(millisecond, 34)
        result = BASE_34_ALPHABET[r] + result
    return result or "0"

def base34_to_int(string: str) -> int:
    BASE_34_ALPHABET = "0123456789ABCDEFGHJKLMNPQRSTUVWXYZ"
    result = 0
    for char in string:
        result = result *34 + BASE_34_ALPHABET.index(char)
    return result