def binarySearch(arr, target):

    n= len(arr)
    s=0
    e=n-1

    while(s<=e):

        mid= (s+e)//2

        if arr[mid]==target:
            return mid
        elif target>arr[mid]:
            s=mid+1
        else:
            e=mid-1
    return -1

arr=[2, 5, 8, 12, 16, 23, 38]
target=16

check1=binarySearch(arr, target)
print(check1)
