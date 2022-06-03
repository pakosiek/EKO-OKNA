#!/usr/bin/env python
import struct

class MD4:
    block_size = 512
    def __init__(self, msg):
        self.msg_encode = msg.encode()
        n = len(self.msg_encode) * 8
        self.msg_encode += b"\x80"
        self.msg_encode += b"\x00" * ((MD4.block_size - (n + 8 + 64) % MD4.block_size)//8)
        self.msg_encode += struct.pack("<Q", n)

        n_extended = len(self.msg_encode)

        self.chunks = [self.msg_encode[i:i+n_extended//8] for i in range(0, len(self.msg_encode), n_extended//8)]

