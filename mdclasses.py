from __future__ import annotations
from typing import Callable, Tuple
from abc import abstractclassmethod
import struct
import math

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
    def code(self) -> str:
        pass


class MD4(MDBase) :
    def __init__(self, msg: str = "") -> None :
        super().__init__(txt)
        
    @staticmethod
    def F(x, y, z) -> bytes :
        return (x & y) | ((~x) & z)

    @staticmethod
    def G(x, y, z) -> bytes :
        return (x & y) | (y & z) | (x & z)

    @staticmethod
    def H(x, y, z) -> bytes :
        return x^y^z

    def code(self):
        
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
        super().__init__(txt)

    def _next_properties(self) -> Tuple[Callable[[int, int, int], int], int, int, int]:
        for i in range(0, 64):
            y = math.floor(2**32 * abs(math.sin(i+1)))
            if i in range(0, 16):
                f = lambda x, y, z: (x & y) | ((~z) & y)
                z = i
                if i % 4 == 1:
                    w = 12
                elif i % 4 == 2:
                    w = 17
                elif i % 4 == 3:
                    w = 22
                else:
                    w = 7
            if i in range(16, 32):
                f = lambda x, y, z: (x & z) | (y & (~z))
                z = (5*i + 1) % 16
                if i % 4 == 1:
                    w = 9
                elif i % 4 == 2:
                    w = 14
                elif i % 4 == 3:
                    w = 20
                else:
                    w = 5
            if i in range(32, 48):
                f = lambda x, y, z: x ^ y ^ z
                z = (3*i + 5) % 16
                if i % 4 == 1:
                    w = 11
                elif i % 4 == 2:
                    w = 16
                elif i % 4 == 3:
                    w = 23
                else:
                    w = 4
            if i in range(48, 64):
                f = lambda x, y, z: z ^ (x | (~z))
                z = (7*i) % 16
                if i % 4 == 1:
                    w = 10
                elif i % 4 == 2:
                    w = 15
                elif i % 4 == 3:
                    w = 21
                else:
                    w = 6
            yield(f, y, z, w)



    def code(self) -> str:
        (A0, B0, C0, D0) = (self._a0, self._b0, self._c0, self._d0)
        for chunk in self._next_block():
            X = struct.unpack("<16I", chunk)
            (A, B, C, D) = (A0, B0, C0, D0)
            for (f, y, z, w) in self._next_properties():
                F = (B + self._left_rotate(A + f(B, C, D) + X[z] + y & 0xFFFFFFFF, w)) & 0xFFFFFFFF
                (A, D, C, B) = (D, C, B, F)
            A0 = (A0 + A) & 0xFFFFFFFF
            B0 = (B0 + B) & 0xFFFFFFFF
            C0 = (C0 + C) & 0xFFFFFFFF
            D0 = (D0 + D) & 0xFFFFFFFF
        wynik = ""
        for b in struct.pack("<4L", A0, B0, C0, D0):
            wynik += "{:02x}".format(b)
        return wynik