# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    for i in range(0, len(arr) ):
        cur_index = i
        smallest_index = cur_index
        j=cur_index
        print(f'before while i={i} j={j} j-1= {arr[j-1]} cur={arr[cur_index]}')
        while j > 0 and arr[j-1] => arr[smallest_index-1]:
            print(f'inside j-1={arr[j-1]}, cur={arr[cur_index]}')
            j=j-1

        if j>0 :
            print(f'before swap smallest=arr[smallest_index]} j={arr[j]}')
            tempj=arr[j]
            arr[j]=arr[smallest_index]
            while j < cur_index:
                temp2 = arr[j+1]
                arr[j+1]=temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr