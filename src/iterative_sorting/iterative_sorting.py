# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        j=cur_index
        while j > 0 and arr[j-1] <= arr[smallest_index]: #loop until j no longer smaller
            print(arr[j], arr[smallest_index])
            j=j-1
        # TO-DO: swap
        print(f'before swap {arr[smallest_index]} {arr[j-1]}')
        arr[smallest_index]=arr[j-1] # j is smaller than smallest
        arr[j-1]=arr[cur_index]
        print(f'swap {arr[smallest_index]} {arr[j-1]}')

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr