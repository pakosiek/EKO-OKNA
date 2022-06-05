#!/usr/bin/env python
import mdclasses
import doctest

def test(a : str, fromfile = False):

    """
    >>> test("slava ukraini")
    063fb87bba4a700330a9eb8030b61081
    >>> test("")
    31d6cfe0d16ae931b73c59d7e0c089c0
    >>> test("./minecraft.exe", True)
    Traceback (most recent call last):
    ...
    mdclasses.OpenFileError: File did not open!
    >>> test("./uml/rsaclasses.png", True)
    620c46fa68b8401b618e455b3126e24c
    >>> test("p")
    9acf4d2875de4fc4de1f34c05d50c110
    >>> test("692137420")
    0bc0d7f1849e8326f547252bed45a3eb
    >>> test("съешь же ещё этих мягких французских булок, да выпей чаю")
    16d7a9ddd4dbd0dea08aabbf4a12b5ee
    >>> test("")
    31d6cfe0d16ae931b73c59d7e0c089c0
    """

    if fromfile:
        var = mdclasses.MD4.load_from_file(a)
    else:
        var = mdclasses.MD4(a)

    var.code()

doctest.testmod(verbose=True)
    
