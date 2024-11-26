import random
import string

def kocok(jumlah:int) -> int:
    kocok_str = ''.join(random.choice(string.ascii_letters) for i in range(jumlah))
    return kocok_str