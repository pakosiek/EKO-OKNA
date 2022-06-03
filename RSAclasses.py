from typing import Tuple
import random
import math
import pickle
import os.path

class IsNotPrime(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    def __str__(self) -> str:
        return "Given Number Is NOT PRIME!"

class MessageToLarge(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    def __str__(self) -> str:
        return "Message is larger than n!"

class rsa:
    def __init__(self, primes: Tuple[int, int] = None, prime_len = None) -> None:
        (p, q) = (None, None)
        if (primes):
            if (not self.__is_prime(primes[0])): raise IsNotPrime
            if (not self.__is_prime(primes[1])): raise IsNotPrime
            (p, q) = primes
        else: 
            if (prime_len): (p, q) = self.__find_primes(prime_len)
            else: (p, q) = self.__find_primes()
        self.__n = p * q
        phi = (p - 1) * (q - 1)
        e = random.randrange(1, phi)
        gcd = math.gcd(e, phi)
        while gcd != 1:
            e = random.randrange(1, phi)
            gcd = math.gcd(e, phi)
        self.__e = e
        self.__d = self.__euclides(e, phi, 1)[0] % phi   

#                              _____     ____
#                            /      \  |  o | 
#                            |        |/ ___\| 
#                            |_________/     
#                            |_|_| |_|_|
       

    @staticmethod
    def __xgcd(a: int, b: int) -> Tuple[int, int, int]:
        c1 = 0
        d1 = 0
        c2 = 1
        d2 = 1
        while b > 0:
            q = a // b
            r = a - b * q
            c = c2 - q * c1
            d = d1 - q * d2
            a = b
            b = r
            c2 = c1
            d1 = d2
            c1 = c
            d2 = d
        gcd = a
        c = c2
        d = d1
        return (gcd,c,d)

    @staticmethod
    def __euclides(a: int, b: int, c: int) -> Tuple[int, int]:
        if c%math.gcd(a, b)==0:
            A = rsa.__xgcd(a, b)
            return (A[1]*(c//A[0]), A[2]*(c//A[0]))
        return None

    @staticmethod
    def __is_prime(value: int, k: int = 20) -> bool:
        if (value == 2): return True
        if (value % 2 == 0): return False
        (s, d) = (0, value - 1)
        while (d % 2 == 0):
            d //= 2
            s += 1
        for i in range(1, k+1):
            a = random.randrange(2, value)
            if (pow(a, d, value) != 1):
                for r in range(0, s):
                    is_p = True
                    if (pow(a, d * pow(2, r), value) == value - 1):
                        is_p = False
                        break
                if (is_p): return False
        return True

    @staticmethod
    def __find_primes(num_of_bits: int = 1024) -> Tuple[int, int]:
        a = random.randrange(2**(num_of_bits-1), 2**num_of_bits)
        while not rsa.__is_prime(a):
            a = random.randrange(2**(num_of_bits-1), 2**num_of_bits)
        b = random.randrange(2**(num_of_bits-1), 2**num_of_bits)
        while not rsa.__is_prime(b):
            b = random.randrange(2**(num_of_bits-1), 2**num_of_bits) 
        return(a,b)

    @staticmethod
    def code(value: int, public_key: Tuple[int, int]) -> int :
        if value > public_key[0]:
            raise MessageToLarge
        return pow(value, public_key[1], public_key[0])

    @staticmethod
    def decode(value: int, private_key: Tuple[int, int]) -> int :
        if value > private_key[0] :
            raise MessageToLarge
        return pow(value, private_key[1], private_key[0])

    @property
    def public_key(self) -> Tuple[int, int]:
        return (self.__n, self.__e)

    @property
    def private_key(self) -> Tuple[int, int]:
        return (self.__n, self.__d)

class DataBaseRSAKey:
    def __init__(self, path: str = "") -> None:
        if (len(path) == 0): path = "keys.DB"
        self.__path = path
        if (os.path.exists(self.__path)):
            f = open(self.__path, "rb")
            self.__arr = pickle.load(f)
            f.close()
        else:
            self.__arr = dict()

    def __del__(self) -> None:
        f = open(self.__path, "wb")
        pickle.dump(self.__arr, f)
        f.close()

    def add(self, id: str, rsa_keys: rsa) -> bool:
        if id in self.__arr:
            return False
        else: 
            self.__arr.update({id: rsa_keys})
            return True

    def remove(self, id: str) -> bool:
        if id in self.__arr: 
            del self.__arr[id]
            return True
        else: return False