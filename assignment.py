#! python3

import math

def tempConversion(degrees, unit="a"):
    degrees=float(degrees) 
    if unit=="C":
        x=(degrees*(9/5) )+ 32
    elif unit=="F":
        x=(degrees-32)/1.8
    return round(x,1)

def factorPair(a,b):
    x=a/b
    factor_list=[]
    factor_list.append(b)
    factor_list.append(x)
    
    return factor_list



def cosineLaw(a,b,c, by="oppositeSide"):
    import math 
        "oppositeSide"==True:
        side1=a
        side2=b
        angle=c


    
  
    
#def toRadians():

#def solution():

#def quadratic():

