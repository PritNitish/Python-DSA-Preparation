def longestSubstring(s):

    n= len(s)
    max_count=0
    
    for i in range(n):
        result=""
        count=0

        for j in range(n):
            if s[j] in result:
                break

            result+=s[j]
            count+=1

        if count>max_count:
            max_count=count

    return max_count

s = "abcabcbb"

check1 = longestSubstring(s)
print(check1)


def checkStringRotation(str1, str2):
    if len(str1)!=len(str2):
        return False

    if str2 in str1+str2:
        return True
    
str1 = "abcd"
str2 = "cdab"

check2=checkStringRotation(str1,str2)
print(check2)

def StringCompression(s):

    n = len(s)
    result = ""
    i = 0

    while i < n:
        count = 1

        while i + 1 < n and s[i] == s[i + 1]:
            count += 1
            i += 1

        result += s[i] + str(count)
        i += 1

    return result


s = "aaabbcd"
check3 = StringCompression(s)
print(check3)


def StringDecompression(string):
    result=""

    for i in range(0,len(string),2):
        char=string[i]
        count=int(string[i+1])
        result+=char*count

    return result

s = "a3b2c1d1"

check4 = StringDecompression(s)
print(check4)

def removeDuplicates(s):

    result=""

    for i in range(len(s)):

        if s[i] not in result:
            result+=s[i]

    return result

s = "programming"
check5=removeDuplicates(s)
print(check5)


def reverseSent(sent):

    words = []
    word = ""

    for i in range(len(sent)):

        if sent[i] != " ":
            word += sent[i]

        else:
            words.append(word)
            word = ""

    words.append(word)

    result = ""

    for i in range(len(words)):
        result = words[i] + " " + result

    return result.strip()


sent = "I love Python"

check6 = reverseSent(sent)
print(check6)


def longestPrefix(arr):

    prefix = ""

    for j in range(len(arr[0])):

        for i in range(1, len(arr)):

            if arr[i][j] != arr[0][j]:
                return prefix

        prefix += arr[0][j]

    return prefix

arr = ["flower", "flow", "flight"]

check7=longestPrefix(arr)
print(check7)


def countCharInString(s):

    result = ""

    for i in range(len(s)):

        if s[i] not in result:

            count = 1

            for j in range(i + 1, len(s)):

                if s[i] == s[j]:
                    count += 1

            print(s[i] + ":" + str(count))

            result += s[i]


Input = "programming"

check8 = countCharInString(Input)
print(check8)


def checkBalance(s):
    count=0

    for i in range(len(s)):
        if s[i]=="(":
            count+=1

        elif s[i]==")":
            count-=1

        if count < 0:
            return False


    if count==0:
        return True

    return False

s = "())("

check9 = checkBalance(s)
print(check9)

def findDuplicateChar(s):

    n= len(s)

    result=""

    for i in range(n):
        count=1
        for j in range(i+1,n):

            if s[i]==s[j]:
                count+=1
        if count>1:
            if s[i] not in result:
                result+=s[i]

    return result

s= "aabbcc"

check10=findDuplicateChar(s)
print(check10)

def firstUniqueChar(s):

    n= len(s)
    result=""

    for i in range(n):
        count=0
        for j in range(n):
            if s[i]==s[j]:
                count+=1

        if count==1:
            return s[i]
        
    return False

Input="leetcode"

check11=firstUniqueChar(Input)
print(check11)

def commonSubstring(s1, s2):

    if s2 in s1:
        return True

    if s1 in s2:
        return True

    return False


s1 = "hello"
s2 = "ell"

check12 = commonSubstring(s1, s2)
print(check12)


def commonSubstring(s1, s2):

    if len(s1) < len(s2):
        temp = s1
        s1 = s2
        s2 = temp

    for i in range(len(s1) - len(s2) + 1):

        count = 0

        for j in range(len(s2)):

            if s1[i + j] == s2[j]:
                count += 1

        if count == len(s2):
            return True

    return False

s1 = "hello"
s2 = "ell"

check13 = commonSubstring(s1, s2)
print(check13)


def stringToInteger(s):

    result = 0
    digits = "0123456789"

    for i in range(len(s)):

        for j in range(10):

            if s[i] == digits[j]:
                result = result * 10 + j

    return result


s = "123"

check14= stringToInteger(s)
print(check14)


def longestPalindrome(s):

    n= len(s)
    longest=""

    for i in range(n):
        for j in range(i+1,n+1):
            sub=s[i:j]

            reverse=""
            for k in range(len(sub)):
                reverse=sub[k]+reverse

            if sub==reverse:
                if len(sub)>len(longest):
                    longest=sub

    return longest

s = "babad"

check15 = longestPalindrome(s)
print(check15)


def isIsomorphic(s1, s2):

    if len(s1) != len(s2):
        return False

    for i in range(len(s1)):

        for j in range(i):
            if s1[i] == s1[j]:
                if s2[i] != s2[j]:
                    return False

            if s2[i] == s2[j]:
                if s1[i] != s1[j]:
                    return False

    return True

s1 = "egg"
s2 = "add"

check16= isIsomorphic(s1, s2)
print(check16)