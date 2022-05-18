#!/usr/bin/env python3

import struct 
from __future__ import annotations
from abc import abstractclassmethod
from typing import Callable, Tuple


class MDBase:


    def __init__(self, txt: str ="",form_file: bool = False) -> None:
        
        self.is_from_file = from_file
        self.content = txt
        

            
        self._a0 = 0x67452301
        self._b0 = 0xEFCDAB89
        self._c0 = 0x98BADCFE
        self._d0 = 0x10325476
        