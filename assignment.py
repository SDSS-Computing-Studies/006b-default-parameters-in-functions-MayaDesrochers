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

def cosineLaw(a,b,angle, oppositeSide=True):
    a=float(a)
    b=float(b)
    angle=toRadians(angle)
     
    if oppositeSide==True:

        side_c= (a**2 + b**2)-(2*a*b*math.cos(angle))
        side_c=math.sqrt(side_c)
        return side_c 

    elif oppositeSide==False:
        if a>b:
            a1 = 1
            b1 = (-2*b*math.cos(angle))
            c1 = (b**2 - a**2)

            x1_and_x2 = quadratic(a1,b1,c1)
            side_c = solution(x1_and_x2)
            return side_c 
    
        if b>a:
            a1 = 1
            b1 = (-2*a*math.cos(angle))
            c1 = a**2 - b**2 

            x1_and_x2 = quadratic(a1,b1,c1)
            side_c = solution(x1_and_x2)
            return side_c 

def toRadians(angle):
    angle=float(angle)
    radians=(angle*math.pi)/180
    return radians

def solution(answerList):
    answer=answerList.pop(1)
    return answer

def quadratic(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    discriminant = math.sqrt((b**2)-(4*a*c))

    answer1 = (-b + discriminant)/(2*a)
    answer2 = (-b - discriminant)/(2*a)
    answerList = [answer1, answer2]
    answerList.sort()
    return answerList
