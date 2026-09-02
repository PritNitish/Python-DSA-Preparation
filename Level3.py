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

        


