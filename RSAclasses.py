#!/usr/bin/env python



# to co zakomentowałem to nie jestem pewien, czy jest zgodne z zamysłem  i czy nie trzeba tego zrobić inaczej

from typing import Tuple


class RSA:
    def __init__(self, pries: Tuple[int, int] = None) -> None:
        self.pries = pries
        #elf.e = self.d = self.p = self.q = self.phi = 0

        n: int = 
        d: int =
        e: int =

    #instance_MessageToLarge = MessageToLarge()
    #instance_IsNotPrime = IsNotPrime()

    @property
    def _code(value: int, public_key: Tuple[int, int]) -> int :
        
        if value > n:
            #instance_MessageToLarge()
        else
            return (self.n, self.e)


    @property
    def _decode(value: int, private_key: Tuple[int, int]) -> int :
        if value > n:
            #instance_MessageToLarge()
        else
            return (self.n, self.d)




    @classmethod
    def public_key(self) -> Tuple[int, int]:


    @classmethod
    def private_key(self) -> Tuple[int, int]:



class IsNotPrime:
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    def __str__(self) -> str:
        return "Given Number Is NOT PRIME!"




class MessageToLarge:
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    def __str__(self) -> str:
        return "Message is larger than n!"

