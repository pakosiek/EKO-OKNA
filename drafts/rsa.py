#!/usr/bin/env python

from abc import abstractmethod
import math
import random

class RSA:

    @staticmethod
    def xgcd(a, b):
        if b==0:
            return (a, 1, 0)
        else:
            (gcd, x_prim, y_prim) = RSA.xgcd(b, a%b)
            return (gcd, y_prim, x_prim-a//b*y_prim)

    @staticmethod
    def euclides(a, b, c):
        if c%math.gcd(a, b)==0:
            A = RSA.xgcd(a, b)
            return (A[1]*(c/A[0]), A[2]*(c/A[0]))
        return None

    @staticmethod
    def czy_pierwsza(n):
        if n < 2:
            return False
        k = 2
        while k*k <= n:
            if n%k == 0:
                return False
            k += 1
        return True

    @staticmethod
    def pierwsze(N):
        wynik = []
        n = 1
        while n<N:
            if RSA.czy_pierwsza(n):
                wynik.append(n)
            n +=1
        return wynik

    # def algorytm_rsa(n=1000000):
    #     prime = RSA.pierwsze(n)
    #     p = random.choice(prime)
    #     q = random.choice(prime)
    #     z = p*q
    #     fi = (p-1)*(q-1)
    #     for el in range(2, fi):
    #         if math.gcd(el, fi) == 1:
    #             e = el
    #             break
    #     (d, x) = RSA.euclides(e, fi, 1)
    #     return ((int(z), int(e)), (int(z), int(d)))
