from __future__ import annotations
from typing import Callable, Tuple
from abc import abstractclassmethod

class MDBase:
    def __init__(self, txt: str ="",form_file: bool = False) -> None:
        
        self.is_from_file = from_file
        self.content = txt
        

            
        self._a0 = 0x67452301
        self._b0 = 0xEFCDAB89
        self._c0 = 0x98BADCFE
        self._d0 = 0x10325476
        
    @classmethod
    def load_from_file(cls, path: str) -> MDBase:
        pass
    def _next_block() -> bytes:
        pass
    def _left_rotate(val: int, shift: int) -> int:
        pass
    @abstractclassmethod
    def _next_properties() -> Tuple[Callable[[int, int, int], int], int, int, int]:
        pass
    @abstractclassmethod
    def _code() -> str:
        pass
    

class MD4 :
    def __init__(self, txt):
        self.txt_encode = txt.encode()
        n = len(self.txt_encode) * 8        

        #super używamy dopiero przy algorytmie
        #tutaj ta część z lib struct, to maksym zrób


        n_extended = len(self.msg_encode)

        self.chunks = [self.txt_encode[i:i+n_extended//8] for i in range(0, len(self.txt_encode), n_extended//8)]
        #prawdopodobie trzeba jeszcze zaimportowaća0,b0,c0,d0, ale to adrian musi potwierdzić czy tak chce, bo będzie narzekał na ram