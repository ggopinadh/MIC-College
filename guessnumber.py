# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 15:50:49 2021

@author: ggopi
"""

import random

def check(r,n):
    if(r==n):
        return 1
    else:
        if(n>r):
            print("Entered Number is Greater than Random Number!")
            return 0
        else:
            print("Entered Number is Lesser than Random Number!")
            return 0
       
r=random.randint(0, 21)
n=int(input("Guess The Number:"))
count=1
result=check(r,n)
while(result!=1):
    count+=1
    n=int(input("Guess The Number:"))
    result=check(r, n)
if(count<=1):
    print("Success!")
else:
    print("You are used",count,"chances to Guess the number",r)