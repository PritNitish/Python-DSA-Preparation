def binarySearch(arr, target):

    n= len(arr)
    start=0
    end=n-1
    while(start<=end):
        mid= (start)+(end-start)//2

        if arr[mid]==target:
            return mid
        elif target>arr[mid]:
            start=mid+1

        else:
            end = mid-1

    return -1


arr=[2, 5, 8, 12, 16, 23, 38]
target=16

check1=binarySearch(arr, target)
print(check1)

def firstAndLast(arr, target):

    n= len(arr)

    first=-1
    last=-1
    # First Occurance
    start=0
    end=n-1
    while(start<=end):

        mid = start+ (end-start)//2

        if arr[mid]==target:
            first=mid
            end = mid-1
        elif target>arr[mid]:
            start = mid+1

        else:
            end =  mid-1

    # Last Occurance
    start = 0
    end = n - 1
    while(start<=end):

        mid=start+(end-start)//2

        if arr[mid]==target:
            last=mid
            start=mid+1
        elif target>arr[mid]:
            start=mid+1
        else:
            end=mid-1

    return first, last
          
arr = [1, 2, 2, 2, 4, 5, 6]
target = 2

check2 = firstAndLast(arr, target)
print(check2)

