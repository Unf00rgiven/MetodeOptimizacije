import numpy as np

def fibonaci_broj(n):
    if n==1 or n==2:
        f=1
    else:
        fp=1
        fpp=1
        for i in range(3,n+1):
            f=fp+fpp
            fpp=fp
            fp=f
    return f
