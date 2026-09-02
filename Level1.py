def reverseString(str):
    n= len(str)
    result=""
    for i in range(n):
        result=str[i]+result

    return result

string1="nitish"
check1=reverseString(string1)
print(check1)

def reverseInteger(num):

    rem=0
    sum=0
    while(num!=0):
        rem=num%10
        sum=sum*10+rem
        num=num//10
    return sum

num=567
check2=reverseInteger(num)
print(check2)

def isPalindromeStr(str):
    n= len(str)
    for i in range(n//2):
        if str[i]!=str[n-i-1]:
            return False
   
    return True

string= "hiih"
check3=isPalindromeStr(string)
print(check3)

def isPalindromeNum(num):
    temp=num
    rem=0
    sum=0
    while(num!=0):

        rem=num%10
        sum=sum*10+rem
        num=num//10

    if(sum==temp):
        return True
    else:
        return False

num = 51151

check4=isPalindromeNum(num)
print(check4)

def isAnagram(str1, str2):
    if len(str1)!=len(str2):
        return False

    for i in range(len(str1)):
        if str1.count(str1[i]) != str2.count(str1[i]):
            return False
    return True

str1="listen"
str2="silent"

check5=isAnagram(str1,str2)
print(check5)


def firstNonRepeating(str):

    for i in range(len(str)):
        count=0
        for j in range(len(str)):
            if str[i]==str[j]:
                count+=1
        if count==1:
            return str[i]

    return None

input="aaabbcde"
check6=firstNonRepeating(input)
print(check6)

def charFreq(s):
    for i in range(len(s)):
        count = 0

        for j in range(len(s)):
            if s[i] == s[j]:
                count += 1

        print(s[i], "→", count)

string = "hello"
check7 = charFreq(string)
print(check7)

def countVowelConsonants(str):

    n= len(str)
    vowel_count=0
    consonent_count=0
    vowel="aeiou"
    for i in range(n):
        if str[i] in vowel:
            vowel_count+=1
        elif str[i].isalpha():
            consonent_count+=1

    return vowel_count, consonent_count
string = "helloi"
check8=countVowelConsonants(string)
print(check8)

def reverseWords(s):

    result = ""
    word = ""

    for i in range(len(s)):
        if s[i] != " ":
            word = word + s[i]

        else:
            result = word + " " + result
            word = ""

    result = word + " " + result

    return result


sent = "I love Python"

check10 = reverseWords(sent)
print(check10)

def removeDuplicate(arr):

    result=[]
    for i in range(len(arr)):
        if arr[i] not in result:
            result.append(arr[i])

    return result

arr=[1,2,2,3,1]
check11=removeDuplicate(arr)
print(check11)

def findDuplicate(arr):

    result=[]

    for i in range(len(arr)):
        count=1
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                count=count+1

        if count>1:
            result.append(arr[i])
    return result

arr = [1, 2, 3, 2, 4, 1, 5]
check12=findDuplicate(arr)
print(check12)

def findSecondLargest(arr):
    first=float("-inf")
    sec=float("-inf")

    for i in range(len(arr)):
        if arr[i]>first:
            sec=first
            first=arr[i]

        elif arr[i]>sec:
            sec= arr[i]

    return sec
arr = [10, 5, 8, 20, 15]
check13=findSecondLargest(arr)
print(check13)

def findSecondSmallest(arr):

    first=float("inf")
    sec=float("inf")

    for i in range(len(arr)):
        if arr[i]<first:
            sec=first
            first=arr[i]
        elif arr[i]<sec:
            sec=arr[i]

    return sec
arr = [10, 5, 8, 20, 15]
check14=findSecondSmallest(arr)
print(check14)
    
def secondMostFreq(arr):

    result = []

    for i in range(len(arr)):
        count = 0

        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1

        if count not in result:
            result.append(count)

    first = float("-inf")
    sec = float("-inf")

    for i in range(len(result)):
        if result[i] > first:
            sec = first
            first = result[i]

        elif result[i] > sec:
            sec = result[i]

    for i in range(len(arr)):
        count = 0

        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1

        if count == sec:
            return arr[i]

    return None


arr = [1, 2, 2, 3, 3, 3, 4]

check15 = secondMostFreq(arr)
print(check15)


def findMissingNum(arr):
    n= len(arr)+1
    sum=n*(n+1)//2
    arr_sum=0

    for i in arr:
        arr_sum+=i

    return sum-arr_sum

arr = [1, 2, 4, 5, 6]
check16=findMissingNum(arr)
print(check16)

def maxMin(arr):
    max=float('-inf')
    min=float("inf")

    for i in range(len(arr)):
        if arr[i]>max:
            max=arr[i]

        if arr[i]<min:
            min=arr[i]

    return max, min

arr = [10, 5, 8, 20, 15]
check17=maxMin(arr)
print(check17)                                   

def isArmstrong(num):

    n= len(str(num))

    rem=0
    sum=0
    temp=num
    while(num!=0):
        rem=num%10
        sum=sum+rem**n
        num=num//10


    if(temp==sum):
        return True
    else:
        return False

num=153
check18=isArmstrong(num)
print(check18)

def isPrime(num):

    if num<2:
        return False
    count=0
    for i in range(2,num//2+1):
        if num%i==0:
            count+=1

    if count>0:
        return False

    return True

num=17
check19=isPrime(num)
print(check19)

def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

    return None
n = 7
check20=fibonacci(n)
print(check20)

def fact(num):
    fact=1
    if num==0:
        return 1
    for i in range(1,num+1):
        fact=fact*i

    return fact
check21=fact(6)
print(check21)

def gcd(num1, num2):

    gcd = 1

    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i

    return gcd


num1 = 12
num2 = 18

check22 = gcd(num1, num2)
print(check22)

def findLcm(num1, num2):

    if num1 > num2:
        start = num1
    else:
        start = num2

    for i in range(start, num1 * num2 + 1):
        if i % num1 == 0 and i % num2 == 0:
            return i


num1 = 4
num2 = 6

check23 = findLcm(num1, num2)
print(check23)

def sumDigit(num):
    sum=0
    while(num!=0):
        rem =num%10
        sum+=rem
        num=num//10

    return sum
num=12345
check24=sumDigit(num)
print(check24)

