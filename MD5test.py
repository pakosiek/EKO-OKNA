#!/usr/bin/env python
import mdclasses
import doctest

def MD5_test(a : str, fromfile = False):

    """
    >>> MD5_test("programowanie obiektowe")
    '80748920af19fc43d240eec073931790'
    >>> MD5_test("./mdclasses.py", True)
    '2e9777bb5dcb7a6e9d19e2504d42bbc1'
    >>> MD5_test("./xyz.exe", True)
    Traceback (most recent call last):
    ...
    mdclasses.OpenFileError: File did not open!
    >>> MD5_test("Jestem z Polski, pierogi są bardzo dobre i kocham jeść.")
    '7bc8ba7a629844cf89478203b9395457'
    >>> MD5_test("Jestem z Polski, pierogi są bardzo dobre i kocham je jeść.")
    'b187d565697f29ca5d959ca8030f78fc'
    >>> MD5_test("")
    'd41d8cd98f00b204e9800998ecf8427e'
    >>> MD5_test("./uml/rsaclasses.png", True)
    '56a05311a8411882625a21f10d2c81b5'
    >>> MD5_test("1234")
    '81dc9bdb52d04dc20036dbd8313ed055'

    """
    
    if fromfile:
        var = mdclasses.MD5.load_from_file(a)
    else:
        var = mdclasses.MD5(a)

    return var.code()

doctest.testmod()