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
    >>> test("“轻轻一拖 音乐流转”中展示的音乐流转功能，支持的音箱设备包括：小米智能家庭屏 10（系统版本MIUI Home 2.1.5及以上）、Xiaomi Sound（音箱系统版本1.76.1及以上）、小米AI音箱（第二代）（音箱系统版本1.76.1及以上）、小米小爱音箱（音箱系统版本1.80.1及以上）、小米小爱音箱Pro（音箱系统版本1.80.1及以上）、Redmi小爱触屏音箱 8（音箱系统版本MIUI Home 2.1.5及以上）、Redmi小爱触屏音箱Pro 8（音箱系统版本MIUI Home 2.1.5及以上）、小米小爱音箱触屏版Pro 8（音箱系统版本MIUI Home 2.1.5及以上），支持的电视设备包括：小米电视全⾯屏Pro 43/55/65英寸、小米电视5及小米电视5Pro 55/65/75英寸、Redmi智能电视 MAX 86/98英寸 、小米透明OLED电视 55英寸、小米电视大师 82英寸/OLED 65英寸、Redmi智能电视 X50/X55/X65/X75（2022款）、小米电视ES 43/50/55/65/75英寸、小米电视6 OLED 55/65英寸。")
    b38d545f9449fd186c0f4e5e5bfec3b6
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
    
