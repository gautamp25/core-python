# binary search
'''Binary search is searching algorithm used in sorted array by repeatedly dividing the search item in half
Time complexity-O(Log n) '''
# with recursive approach
def binary_ser(arr,l,r,x):
    if r >= l:
        # get mid
        mid = l + (r-1) // 2
        # print(mid)
        if arr[mid] == x:
            return mid
        # if element is smaller than mid, then it is present in left subarray
        elif arr[mid] > x:
            return binary_ser(arr, l, mid-1, x)
        # if element is greater than mid, then it is presr=ent in right subarray
        else:
            return binary_ser(arr, mid+1, r, x)
    else:
        # if element is not present in array
        return -1
    
arr=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50] 
x = 40
res = binary_ser(arr, 0, len(arr)-1, x)
print(f"RES-{res}")

if res != -1:
    print(f"Element present at index :{res}")
else:
    print(f"Element is not present in array")


# with iterative approach
def binary_search(arr, l, r, x ):
    while l <= x:
        mid = l + (r - 1) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x: 
            # if ele is greater than mid then move l by mid+1
            l = mid+1
        else: 
            # if ele is smaller than r then move r by mid-1
            r = mid - 1
    # if ele not present
    return -1

data = [11, 12, 13, 14, 15, 16]
x = 12
result = binary_search(data, 0, len(data)-1, x)
if result != -1:
    print(f"Element is present at index: {result}")
else:
    print(f"Element is not present in an array")

