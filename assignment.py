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

def cosineLaw(side1,side2,angle, side3="oppositeSide"):
    a=side1
    b=side2
    radians=toRadians(angle)
    side3= math.sqrt((a**2)+(b**2)-((2*a*b)*math.cos(radians)))

    return side3

def toRadians(angle):
  
    angle=float(angle)
    radians=(angle*(math.pi))/180
    return radians

def solution(answerList):
    answer=answerList.pop(1)
    return answer

def quadratic(side1, side2, side3):
    answerList=[]
    a=side1
    b=side2
    c=side3
    answer1=((-b)+(math.sqrt((b**2)-(4*a*c))))/(2*a)
    answer2=((-b)-(math.sqrt((b**2)-(4*a*c))))/(2*a)
    answerList.append(answer1)
    answerList.append(answer2)
    answerList.sort()
    return answerList

