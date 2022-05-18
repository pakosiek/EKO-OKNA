#!/usr/bin/env python3

import struct 

class MDBase:

    block_size = 64

    def __init__(self, txt: str ="",form_file: bool = False):
        
        self.from_file = from_file
        self.txt = txt
        if from_file = True:
            # ewentualnie tutaj będzie wywołanie metody
            text = open(txt, "r")

        else:
            
        
        _a0 = 0x67452301
        _b0 = 0xEFCDAB89
        _c0 = 0x98BADCFE
        _d0 = 0x10325476
        