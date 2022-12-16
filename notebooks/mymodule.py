#!/usr/bin/python3
# mymodule.py -- A function and a test
""" This module has the implementation of the pow2 function
"""

def pow2(n):
    """ returns 2**n using left shifts 
    """ 
    return  1<<n


def makeTable(f,low,high):
    """ makes a simple table just for testing the function """
    for i in range(low,high+1):
        print("x=",i,"F(X)=",f(i))

if __name__ == "__main__":
        # place tests here
        makeTable(pow2,1,8)
