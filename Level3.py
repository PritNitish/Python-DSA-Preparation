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






