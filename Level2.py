def twoSum(arr,target):
    n= len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j] == target:
                return i, j


arr = [2, 7, 11, 15]
target = 9
Check1=twoSum(arr, target)
print(Check1)


def threeSum(arr,target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                if arr[i] + arr[j] + arr[k] == target:
                    return i, j, k

arr = [1, 2, 3, 4, 5]
target=9

Check2=threeSum(arr, target)
print(Check2)

def moveZero(arr):
    n=len(arr)
    result1=[]
    result2=[]
    for i in range(n):
        if arr[i]==0:
            result2.append(arr[i])
        else:
            result1.append(arr[i])
    return result1+result2

arr = [0, 1, 0, 3, 12]
Check3=moveZero(arr)
print(Check3)


print("################################ Intersection ##################################")
def interSection(arr1,arr2):
    result=[]
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i]==arr2[j] and arr1[i] not in result:
                result.append(arr1[i])
    return result

arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
Check4=interSection(arr1,arr2)
print(Check4)

def unionArray(arr1, arr2):
    result=[]

    for i in range(len(arr1)):
        if arr1[i] not in result:
            result.append(arr1[i])

    for j in range(len(arr2)):
        if arr2[j] not in result:
            result.append(arr2[j])

    return result


arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 2, 3, 4, 5, 6]

Check5=unionArray(arr1,arr2)
print(Check5)

def mergeTwoArray(arr1,arr2):

    result=[]
    i=0
    j=0

    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j+=1

    while i<len(arr1):
        result.append(arr1[i])
        i+=1
    while j<len(arr2):
        result.append(arr2[j])
        j+=1
    return result
arr1 = [0,1,3, 3, 5, 7]
arr2 = [2, 4, 6, 8]

Check6=mergeTwoArray(arr1,arr2)
print(Check6)

def commonElements(arr1, arr2):

    result=[]

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i]==arr2[j] and arr1[i] not in result:
                result.append(arr1[i])
    return result

arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 2, 4, 6]

Check7=commonElements(arr1,arr2)
print(Check7)


def missingAndDuplicate(arr):

    result=[]
    n=len(arr)
    desired_sum= n*(n+1)//2
    arr_sum=0
    result_sum=0
    for i in range(n):
        if arr[i] not in result:
            result.append(arr[i])

    for i in result:
        result_sum+=i

    for i in arr:
        arr_sum+=i

    missing= desired_sum-result_sum
    duplicate= arr_sum-result_sum

    return missing, duplicate

arr = [1, 2, 2, 4, 5, 6]

Check8= missingAndDuplicate(arr)
print(Check8)

def MajorityElement(arr):

    element = None
    count = 0

    for i in range(len(arr)):

        if count == 0:
            element = arr[i]

        if arr[i] == element:
            count += 1
        else:
            count -= 1

    # Verify majority element
    count = 0

    for i in range(len(arr)):
        if arr[i] == element:
            count += 1

    if count > len(arr) // 2:
        return element

    return None


arr = [2, 2, 1, 1, 1, 1, 2, 2, 2]

Check9 = MajorityElement(arr)
print(Check9)

def maxSubArrSum(arr):
    max_sum = float('-inf')
    current_sum = 0

    for i in range(len(arr)):
        current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum

        if current_sum < 0:
            current_sum = 0

    return max_sum
            
arr = [-2, 5, -1, 2, -3, 4, -10]
Check10=maxSubArrSum(arr)
print(Check10)

def rotateRight(arr,k):

    n=len(arr)
    k=k%n
    result=[]
    for i in range(n-k, n):
        result.append(arr[i])

    for i in range(n-k):
        result.append(arr[i])

    return result

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3


Check11=rotateRight(arr,k)
print(Check11)

def rotateLeft(arr,k):

    n=len(arr)
    k=k%n
    result=[]
    for i in range(k,n):
        result.append(arr[i])

    for i in range(k):
        result.append(arr[i])

    return result

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
Check12=rotateLeft(arr,k)
print(Check12)

def pairSum(arr, target):

    n= len(arr)
    for i in range(n):
        for j in range(i+1,n):

            sum=arr[i]+arr[j]

            if sum==target:
                return arr[i], arr[j]
    
arr = [2, 7, 11, 15]
target = 9

Check13=pairSum(arr, target)
print(Check13)

def pairDiff(arr, target):
    n= len(arr)

    for i in range(n):
        for j in range(i+1,n):

            diff = abs(arr[i]-arr[j])

            if diff==target:
                return arr[i], arr[j]

arr = [5, 20, 3, 2, 50, 80]
target = 78

Check14=pairDiff(arr, target)
print(Check14)

def findLeaders(arr):
    n= len(arr)
    result=[]
    leader=None
    for i in range(n):
        count=0
        for j in range(i+1,n):

            if arr[i]>arr[j]:
                count+=1


        if count==n-i-1:
            result.append(arr[i])
    return result

arr = [16, 0,17,15, 4, 3, 5, 2]
Check15=findLeaders(arr)
print(Check15)

def findEquilibrium(arr):
    n= len(arr)
    total_sum=0
    left_sum=0
    for i in range(n):
        total_sum+=arr[i]

    for j in range(n):
        right_sum= total_sum-arr[j]-left_sum

        if left_sum==right_sum:
            return j
        left_sum+=arr[j]

    return -1

arr = [1, 3, 5, 2, 1, 1]
check16 = findEquilibrium(arr)
print(check16)
            

def prodExceptSelf(arr):

    result = []

    for i in range(len(arr)):
        product = 1

        for j in range(len(arr)):
            if i != j:
                product = product * arr[j]

        result.append(product)

    return result


arr = [1, 2, 3, 4]

check17=prodExceptSelf(arr)
print(check17)


def prodExceptSelf(arr):

    n = len(arr)
    count = 0
    result = []

    # Count zeros
    for i in range(n):
        if arr[i] == 0:
            count += 1

    # More than one zero
    if count > 1:
        return [0] * n

    # One zero
    if count == 1:
        total = 1

        for i in range(n):
            if arr[i] != 0:
                total *= arr[i]

        for i in range(n):
            if arr[i] == 0:
                result.append(total)
            else:
                result.append(0)

        return result

    # No zero
    total = 1

    for i in range(n):
        total *= arr[i]

    for i in range(n):
        result.append(total // arr[i])

    return result


arr = [1, 2, 3, 4,0]

print(prodExceptSelf(arr))
   





        

    

        