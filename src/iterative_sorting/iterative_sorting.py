# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    for i in range(0, len(arr)-1):
        cur_index = i
        smallest_index = cur_index
  
        for j in range(cur_index,len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index=j

        tempj=arr[smallest_index]
        arr[smallest_index]=arr[cur_index]
        arr[cur_index]=tempj


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swapped = True

    while swapped:
        swapped=False
        for i in range(0,len(arr)-1):
            if arr[i] > arr[i+1] :
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
                swapped=True

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr