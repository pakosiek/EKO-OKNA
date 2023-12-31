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

    @abstractclassmethod
    def load_from_file(cls, path: str) -> MDBase:
        '''Initialisation of the class that will be hashing a file of given path.'''
        pass

    def _next_block(self) -> bytes:
        '''Yield a block of data with a length of 64 bytes
           until the end of file or string.'''
        if (self.__is_from_file):
            try: f = open(self.__content, "rb")
            except: raise OpenFileError
            try:
                size = 0
                buffer = f.read(64)
                while (buffer):
                    if (len(buffer) < 64):
                        break   
                    size += 1
                    yield buffer
                    buffer = f.read(64)
                size = ((64 * size) + len(buffer)) * 8
                n = (64 - ((len(buffer) + 9) % 64)) % 64
                buffer += b"\x80" + (n * b"\x00") + struct.pack("<Q", size)
                for i in range(0, len(buffer), 64):
                    yield buffer[i:(i+64)]
            finally: 
                f.close()
        else:
            txt = bytes(self.__content, "utf-8")
            tmp = b""
            for i in range(0, len(txt), 64):
                tmp = txt[i:(i+64)]
                if (len(tmp) < 64): break
                else: yield tmp
            size = len(txt) * 8
            n = (64 - ((len(tmp) + 9) % 64)) % 64
            tmp += b"\x80" + (n * b"\x00") + struct.pack("<Q", size)
            for j in range(0, len(tmp), 64):
                yield tmp[j:(j+64)]

    @staticmethod            
    def _left_rotate(val: int, shift: int) -> int:
        '''An operation on 32-bit integer that moves bits
           from right to left and transfers bits beyond the left boundary
           to the center next to the right boundary.'''
        return ((val << shift) | (val >> (32 - shift))) & 0xFFFFFFFF

    @abstractclassmethod
    def _next_properties(self) -> Tuple[Callable[[int, int, int], int], int, int, int]:
        pass
    
    @abstractclassmethod
    def code(self) -> str:
        pass

class MD4(MDBase):
    '''Class which hashing input data in md4 standard'''
    def __init__(self, txt: str = "", from_file: bool = False) -> None:
        '''Initialisation of the class that will be hashing a given string.'''
        super().__init__(txt, from_file)

    @classmethod
    def load_from_file(cls, path: str) -> MDBase:
        return MD4(txt = path, from_file = True)

    def code(self) -> str:
        '''Returns hash (string representation of 16 bytes / 128 bits) of given data in md4 standard.'''
        (A0, B0, C0, D0) = (self._a0, self._b0, self._c0, self._d0)
        for chunk in self._next_block():
            X = struct.unpack("<16I", chunk)
            (A, B, C, D) = (A0, B0, C0, D0)
            for (f, y, z, w) in self._next_properties():
                F = self._left_rotate(A + f(B, C, D) + X[z] + y & 0xFFFFFFFF, w)
                (A, B, C, D) = (D, F, B, C)
            A0 = (A0 + A) & 0xFFFFFFFF
            B0 = (B0 + B) & 0xFFFFFFFF
            C0 = (C0 + C) & 0xFFFFFFFF
            D0 = (D0 + D) & 0xFFFFFFFF
        wynik = ""
        for b in struct.pack("<4L", A0, B0, C0, D0):
            wynik += "{:02x}".format(b)
        return wynik

    def _next_properties(self) -> Tuple[Callable[[int, int, int], int], int, int, int]:
        '''Yield a tuple (f, y, z, w) 48 times where variables means: \n
           - f: one of functions F, G, H \n
           - y: an integer which is need to by add to result \n
           - z: an integer from range [0,16) meaning index of 4-bytes part of 64-bytes block \n
           - w: a shift for left rotate'''
        for i in range(48):
            if i in range(0, 16):
                f = lambda x, y, z: (x & y) | ((~x) & z)
                y = 0
                z = i
                Wlist = [3, 7, 11, 19]
                w = Wlist[i % 4]
            if i in range(16, 32):
                f = lambda x, y, z: (x & y) | (y & z) | (x & z)
                y = 0x5A827999
                Zlist = [0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15]
                z = Zlist[i-16]
                Wlist = [3, 5, 9, 13]
                w = Wlist[i%4]
            if i in range(32, 48):
                f = lambda x, y, z: x^y^z
                y = 0x6ED9EBA1
                Wlist = [3, 9, 11, 15]
                Zlist = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
                w = Wlist[i % 4]
                z = Zlist[i-32]
            yield (f, y, z, w)

class MD5(MDBase):
    '''Class which hashing input data in MD5 standard'''
    def __init__(self, txt: str = "", from_file = False) -> None :
        '''Initialisation of the class that will be hashing a given string.'''
        super().__init__(txt, from_file)

    @classmethod
    def load_from_file(cls, path: str) -> MDBase:
        return MD5(txt = path, from_file = True)

    def _next_properties(self) -> Tuple[Callable[[int, int, int], int], int, int, int]:
        '''Yield a tuple (f, y, z, w) 64 times where variables means: \n
           - f: one of functions F, G, H, I \n
           - y: an integer which is need to by add to result \n
           - z: an integer from range [0,16) meaning index of 4-bytes part of 64-bytes block \n
           - w: a shift for left rotate'''
        for i in range(0, 64):
            y = math.floor(0x100000000 * abs(math.sin(i+1)))
            if i in range(0, 16):
                f = lambda x, y, z: (x & y) | ((~x) & z)
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
                f = lambda x, y, z: y ^ (x | (~z))
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
        '''Returns hash (string representation of 16 bytes / 128 bits) of given data in md5 standard.'''
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
        result = ""
        for b in struct.pack("<4L", A0, B0, C0, D0):
            result += "{:02x}".format(b)
        return result

