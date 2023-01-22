def bubble_optimized(arr):
    iterations = 0
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            iterations += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr, iterations
    
def insert_sort(arr):
    iterations = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            iterations += 1
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr, iterations
    
def merge_sort_1(arr):
    
    iterations = 0
    sorted_arr = []
    
    while arr:
        min_elm = arr[0]
        for elm in arr:
            iterations += 1
            if elm < min_elm:
                min_elm = elm
        sorted_arr.append(min_elm)
        arr.remove(min_elm)
        
    return sorted_arr, iterations
    
def merge_sort_2(left, right):
    
    iterations = 0
    sorted_arr = []
    
    while min(len(left), len(right)) > 0:
        if left[0] < right[0]:
            sorted_arr.append(left.pop(0))
        else:
            sorted_arr.append(right.pop(0))
    if left:
        sorted_arr += left
    if right:
        sorted_arr += right
    
    return sorted_arr
        
    
            
        
    
        

arr = [9,8,7,6,5,4,3,2,1]
print(bubble_optimized(arr))
arr = [9,8,7,6,5,4,3,2,1]
print(insert_sort(arr))
arr = [9,8,7,6,5,4,3,2,1]
print(merge_sort_1(arr))
left = [2,5,6,10]
right = [3,4,12,20]
print(merge_sort_2(left, right))
