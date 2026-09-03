def isEvenOdd(num):

    if (num&1)==0:
        return "Even"

    return "Odd"

num=8
check1=isEvenOdd(num)
print(check1)

def countSetBits(num):
    count=0
    while(num!=0):
        if (num&1)==1:
            count+=1

        num=num>>1

    return count

num=17
check2=countSetBits(num)
print(check2)

def findOnceOccuring(arr):

    once=0

    for i in arr:
        once= i^once

    return once
arr = [4, 1, 4, 1, 9]
check3=findOnceOccuring(arr)
print(check3)

def missingNum(arr):
    n= len(arr)
   
    mis=0
    for i in range(1,n+2):
        mis=mis^i

    for i in arr:
        mis=mis^i

    return mis
            
arr = [1, 2, 4, 5]
check4= missingNum(arr)
print(check4)

def isPow2(num):
    count=0
    while(num!=0):

        if (num&1)==1:
            count+=1

        num=num>>1
    if count==1:
        return True
    return False

num=8
check5=isPow2(num)
print(check5)


def swapNum(num1, num2):
    num1=num1^num2
    num2=num1^num2
    num1=num1^num2

    return num1, num2

a = 5
b = 10
check6=swapNum(a,b)
print(check6)

def reverseBits(num):

    result=0

    while(num!=0):

        bit= num&1

        result=(result<<1) | bit

        num=num>>1
    return result

num = 13

check7 = reverseBits(num)
print(check7)

    


        

