from __future__ import annotations
from asyncore import write
from typing import Callable, Tuple
from abc import abstractclassmethod
import struct
from typing_extensions import Self

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
        return MDBase(txt = path, from_file = True)

    def _next_block(self) -> bytes:
        if (self.__is_from_file):
            f = open(self.__content, "rb")
            if (f.closed): raise OpenFileError
            try:
                size = 0
                buffer = f.read(64)
                while (buffer):
                    size += 1
                    if (len(buffer) < 64):
                        break    
                    yield buffer
                    buffer = f.read(64)
                size = ((64 * size) + len(buffer)) * 8
                n = 64 - ((len(buffer) + 9) % 64)                      
                buffer += b"\x80" + (n * b"\x00") + struct.pack("<Q", size)
                for i in range(0, len(buffer), 64):
                    yield buffer[i:(i+64)]
            finally: 
                f.close()
        else:
            for i in range(0, len(self.__content), 64):
                tmp = bytes(self.__content[i:(i+64)], "utf-8")
                if (len(tmp) < 64):
                    size = len(self.__content) * 8
                    n = 64 - ((len(tmp) + 9) % 64)                        
                    tmp += b"\x80" + (n * b"\x00") + struct.pack("<Q", size)
                    for j in range(0, len(tmp), 64):
                            yield tmp[j:(j+64)]
                else: yield tmp

    @staticmethod            
    def _left_rotate(val: int, shift: int) -> int:
        return ((val << shift)|(val >> (32 - shift)))&0xFFFFFFFF

    @abstractclassmethod
    def _next_properties(self) -> Tuple[Callable[[int, int, int], int], int, int, int]:
        pass
    
    @abstractclassmethod
    def _code(self) -> str:
        pass


class MD4(MDBase) :
    def __init__(self, msg: str = "") -> None :
        super().__init__(txt = msg)
        self._code()
        
    @staticmethod
    def F(x, y, z) -> bytes :
        return (x & y) | ((~x) & z)

    @staticmethod
    def G(x, y, z) -> bytes :
        return (x & y) | (y & z) | (x & z)

    @staticmethod
    def H(x, y, z) -> bytes :
        return x^y^z

    def _code(self):
        
        for chunk in super()._next_block():
            X = list(struct.unpack("<16I", chunk))
            (A, B, C, D) = (self._a0, self._b0, self._c0, self._d0)
            for i in range(16):
                Wlist = [3, 7, 11, 19]
                y = 0
                t = A + MD4.F(B, C, D) + X[i]
                (A, B, C, D) = (D, MDBase._left_rotate(t, Wlist[n % 4]), B, C)
            for k in range(16):
                y = 0x5A827999
                Wlist = [3, 5, 9, 13]
                Zlist = [0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15]
                t = A + MD4.G(B, C, D) + X[Zlist[i]] + y
                (A, B, C, D) = (D, MDBase._left_rotate(t, Wlist[n % 4]), B, C)
            for l in range(16):
                y = 0x6ED9EBA1
                Wlist = [3, 9, 11, 15]
                Zlist = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
                t = A + MD4.H(B, C, D) + X[Zlist[i]] + y
                (A, B, C, D) = (D, MDBase._left_rotate(t, Wlist[n % 4]), B, C)



class MD5(MDBase) :

    def __init__(self, txt: str = "") -> None :
        self.txt_encode = txt.encode()
        
    @abstractclassmethod
    def _next_properties(self):
        super()._next_properties(self)

    @abstractclassmethod
    def _code():
        super()._code()