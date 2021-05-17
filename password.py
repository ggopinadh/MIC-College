# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 14:51:23 2021

@author: ggopi
"""
    
def check_password(data):
    if(len(data)<8):
        print("Length Must Be 8 Characters or More!")
    else:
        
        for i in data:
            k=ord(i)
            if(k>=65 and k<=90):
                break
            else:
                print("Password Must Contain Atleast 1 Upper Case Letter!")
                break
        for i in data:
            k=ord(i)
            if(k>=97 and k<=122):
                break
            else:
                print("Password Must Contain Atleast 1 Lower Case Letter!")
                
        for i in data:
            k=ord(i)
            if(k>=48 and k<=57):
                pass
            else:
                print("Password Must Contain Atleast 1 Numeric Number!")
                break
        for i in data:
            k=ord(i)
            if((k>=32 and k<=47) or (k>=58 and k<=64) or (k>=91 and k<=96) or (k>=123 and k<=126)):
                pass
            else:
                print("Password Must Contain Atleast 1 Special Character!")
                break
                

data=input("Enter Password:")
check_password(data)

