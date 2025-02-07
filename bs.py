
def bs(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (right + left) // 2  
        if arr[mid] == target:  
            return mid
        elif arr[mid] < target:  
            left = mid + 1
        else:  
            right = mid - 1
    return -1  
arr_input=input("enter array in list acending order by comma")
arr=[int(x) for x in  arr_input.split(",")]
target=int(input("enter target "))
#arr = [1, 3, 4, 5, 11, 17]
#target = 11
result = bs(arr, target)

if result != -1:
    print(f"Item found at index {result}")
else:
    print("Item not present")




