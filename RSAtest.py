import RSAclasses
import doctest



def y(x):
    
    a = RSAclasses.rsa(prime_bits_len= 64)

    """
    >>> RSAclasses.rsa.decode(RSAclasses.rsa.code(12, a.public_key),a.private_key)
    12
    >>> RSAclasses.rsa.decode(RSAclasses.rsa.code(1324, a.public_key),a.private_key)
    1324
    >>> RSAclasses.rsa.decode(RSAclasses.rsa.code(142536475869, a.public_key),a.private_key)
    142536475869
    >>> RSAclasses.rsa.decode(RSAclasses.rsa.code(1595135753, a.public_key),a.private_key)
    1595135753
    >>> RSAclasses.rsa.decode(RSAclasses.rsa.code(314, a.public_key),a.private_key)
    314
    >>> RSAclasses.rsa.decode(RSAclasses.rsa.code(0, a.public_key),a.private_key)
    0
    >>> RSAclasses.rsa.decode(RSAclasses.rsa.code(714065201, a.public_key),a.private_key)
    714065201
    >>> RSAclasses.rsa.decode(RSAclasses.rsa.code(961870723, a.public_key),a.private_key)
    961870723
    >>> RSAclasses.rsa.decode(RSAclasses.rsa.code(56113794, a.public_key),a.private_key)
    56113794
    >>> RSAclasses.rsa.decode(RSAclasses.rsa.code(529816129, a.public_key),a.private_key)
    529816129
    RSAclasses.rsa.decode(RSAclasses.rsa.code(1029384756, a.public_key),a.private_key)
    1029384756
    RSAclasses.rsa.decode(RSAclasses.rsa.code(11111111111, a.public_key),a.private_key)
    11111111111
    RSAclasses.rsa.decode(RSAclasses.rsa.code(128008132, a.public_key),a.private_key)
    128008132
    >>> RSAclasses.rsa.decode(RSAclasses.rsa.code(1504201, a.public_key),a.private_key)
    1504201
    >>> RSAclasses.rsa.decode(RSAclasses.rsa.code(177013, a.public_key),a.private_key)
    177103
    >>> RSAclasses.rsa.decode(RSAclasses.rsa.code(11213785, a.public_key),a.private_key)
    11213785
    """
    return RSAclasses.rsa.decode(RSAclasses.rsa.code(x, a.public_key),a.private_key)



doctest.testmod()