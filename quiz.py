# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 14:19:39 2021

@author: ggopi
"""

def check():
    count=0
    q={"What is the best programming Language?:":"python","What is 2 + 8 + 9 - 1 equals to?:":"18","What OS offers better Security-Android or Apple?:":"apple","Who is the Founder of Python Programming Language?:":"guddio van rossum","What is the current version of Python used?:":"3.8"}
    for i in q:
        print("\n",i,end="")
        ans=input()
        if((ans.lower())==q[i]):
            print("Correct!")
            count+=1
        else:
            print("Incorrect!")
    return count


print("Welcome To Quiz!")
start=input("Are You Insterested in Playing(Yes/No):")
if(start.lower()=="yes"):
    ready=input("Are You Ready!(yes/No):")
    if(ready=="yes"):
        result=check()
        print("Thank you for playing,You have got",result,"questions correct.")
        print("Marks Secured:",result*20.0)
        
        
    else:
        print("Bye! Catch You with another Quiz soon...")
    
    
else:
    print("Bye! Catch You with another Quiz soon...")
    
