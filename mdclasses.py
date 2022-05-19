from __future__ import annotations
from typing import Callable, Tuple
from abc import abstractclassmethod
import struct

class OpenFileError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    def __str__(self) -> str:
        return "File did not open!"

class MDBase:
    def __init__(self, txt: str ="",from_file: bool = False) -> None:
        self.__is_from_file = from_file
        self.__content = txt 
        self._a0 = 0x67452301
        self._b0 = 0xEFCDAB89
        self._c0 = 0x98BADCFE
        self._d0 = 0x10325476

    @classmethod
    def load_from_file(cls, path: str) -> MDBase:
        pass

    def _next_block(self) -> bytes:
        if (self.__is_from_file):
            f = open(self.__content, "rb")
            if (f.closed): raise OpenFileError
            try:
                buffer = f.read(64)
                while (buffer):
                    if (len(buffer) < 64):
                        size = len(buffer) * 8
                        n = 64 - ((len(buffer) + 9) % 64)                      
                        buffer += b"\x80" + (n * b"\x00") + struct.pack("<Q", size)
                        for i in range(0, len(buffer), 64):
                            yield buffer[i:(i+64)]
                    else: yield buffer
                    buffer = f.read(64)
            finally: 
                f.close()
        else:
            for i in range(0, len(self.__content), 64):
                tmp = bytes(self.__content[i:(i+64)], "utf-8")
                if (len(tmp) < 64):
                    size = len(tmp) * 8
                    n = 64 - ((len(tmp) + 9) % 64)                        
                    tmp += b"\x80" + (n * b"\x00") + struct.pack("<Q", size)
                    for j in range(0, len(tmp), 64):
                            yield tmp[j:(j+64)]
                else: yield tmp

    @staticmethod            
    def _left_rotate(val: int, shift: int) -> int:
        pass

    @abstractclassmethod
    def _next_properties(self) -> Tuple[Callable[[int, int, int], int], int, int, int]:
        pass
    
    @abstractclassmethod
    def _code() -> str:
        pass
