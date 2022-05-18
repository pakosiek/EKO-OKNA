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
    