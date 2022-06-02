from typing import Tuple
import random
import math

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

class RSA:
    def __init__(self, pries: Tuple[int, int] = None) -> None:
        pass

    @staticmethod
    def __xgcd(a: int, b: int) -> Tuple[int, int, int]:
        pass

    @staticmethod
    def __euclides(a: int, b: int, c: int) -> Tuple[int, int]:
        pass

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
        pass

    @staticmethod
    def code(value: int, public_key: Tuple[int, int]) -> int :
        pass

    @staticmethod
    def decode(value: int, private_key: Tuple[int, int]) -> int :
        pass

    @property
    def public_key(self) -> Tuple[int, int]:
        return (self.n, self.e)

    @property
    def private_key(self) -> Tuple[int, int]:
        return (self.n, self.d)

