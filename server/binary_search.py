def binary_search(arr, target, left, right):
    # Base case
    if left > right:
        return -1

    # Find the middle index
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid # Found the target
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1) # Recursively search the left half
    else:
        return binary_search(arr, target, mid + 1, right) # Recursively search the right half
    
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = 7
left=0
right=len(arr) - 1

result = binary_search(arr, target, left, right)
if result != -1:
    print(f'Recursive: Element found at index {result}')
else:
    print('Element not found')