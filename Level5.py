def binarySearch(arr, target):

    start=0
    end= len(arr)-1

    while(start<=end):

        mid= start+(end-start)//2

        if arr[mid]==target:
            return mid

        elif target>arr[mid]:

            start = mid+1

        else:
            end = mid-1

    return -1

arr = [2, 5, 8, 12, 16, 23, 38]
target = 16

check1= binarySearch(arr, target)
print(check1)

def firstAndLast(arr, target):

    ##################### First Occurance ##########################

    start=0
    end= len(arr)-1
    first=-1
    last=-1
    while(start<=end):
        mid = start + (end-start)//2

        if arr[mid]==target:
            first=mid
            end = mid-1

        elif target>arr[mid]:
            start= mid+1

        else:
            end = mid-1

    ###################### Last Occurance ###########################


    start=0
    end=len(arr)-1

    while(start<=end):

        mid = start + (end-start)//2

        if arr[mid]== target:

            last =mid
            start = mid+1

        elif target>arr[mid]:
            start= mid+1
        else:

            end = mid-1

    return first, last

arr = [1, 2, 2, 2, 4, 5, 6]
target = 2

check2= firstAndLast(arr, target)
print(check2)

####################  Dekhna hai ########################
def findElement(arr, target):

    start = 0
    end = len(arr) - 1

    while(start <= end):

        mid = start + (end-start)//2

        if arr[mid] == target:
            return mid

        # Left half sorted
        if arr[start] <= arr[mid]:

            if arr[start] <= target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

        # Right half sorted
        else:

            if arr[mid] < target <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1

    return -1


arr = [4, 5, 6, 7, 0, 1, 2]
target = 0

check = findElement(arr, target)
print(check)
###################################################################


def findPeak(arr):

    start= 0
    end= len(arr)-1
    peak =-1
    while(start<end):

        mid = start + (end-start)//2

        if arr[mid]<arr[mid+1]:
            start = mid+1

            peak= start

        else:

            end = mid

    return peak

arr = [1, 3, 20, 4, 1, 0]

check3= findPeak(arr)
print(check3)


def findSqrt(num):

    start= 0
    end = num
    ans=0
    while(start<=end):

        mid = (start+end)//2

        if mid*mid == num:
            ans= mid
            return ans
        elif mid*mid < num:

            start = mid+1
            ans= mid

        else:
            end = mid-1

    return ans

num=17

check4= findSqrt(num)
print(check4)