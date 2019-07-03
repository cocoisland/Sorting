# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    i = j = k = 0
            
    # Copy data to temp arrays from arrA and arrB 
    while i < len(arrA) and j < len(arrB): 
        if arrA[i] < arrB[j]: 
            merged_arr[k] = arrA[i] 
            i+=1
        else: 
            merged_arr[k] = arrB[j] 
            j+=1
        k+=1

    # Checking if any element was left 
    while i < len(arrA): 
        merged_arr[k] = arrA[i] 
        i+=1
        k+=1
        
    while j < len(arrB): 
        merged_arr[k] = arrB[j] 
        j+=1
        k+=1
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
        
    mid = len(arr)//2
    L = merge_sort(arr[:mid])
    R = merge_sort(arr[mid:])

    return merge(L,R)

#a=[5,2,6,8,7,9]
#print(merge_sort(a))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
