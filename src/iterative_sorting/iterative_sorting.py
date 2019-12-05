# TO-DO: Complete the selection_sort() function below 
import timeit

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
   
        # TO-DO: swap (used tuple packing/unpacking)
        swap = arr[cur_index], arr[smallest_index]
        arr[smallest_index], arr[cur_index] = swap
        print(arr)

    return arr
print(f'SELECTION SORT !!!')
testarr = [3,44,38,5,47,15,36,26,27,2,46,4,19,50, 48]
# elapsed_time = timeit.timeit( (selection_sort(testarr)), number = 100)/100
# elapsed_time = timeit.timeit(selection_sort(testarr), number=100)/100
print( selection_sort(testarr) )
# print('Selection sort took:',  elapsed_time)


# TO-DO:  implement the Bubble Sort function below

def bubble_sort( arr ):
    swapped = True
    iteration = len(arr) - 1
    while swapped and iteration > 0:
        swapped: False
        for i in range(0, len(arr)- 1):
            if arr[i] > arr[i + 1]:
                swap = arr[i], arr[i + 1]
                arr[i + 1], arr[i] = swap
                swapped: True
        iteration -= 1
        print(arr)
    return arr

print(f'BUBBLE SORT ')
testarr = [3,44,38,5,47,15,36,26,27,2,46,4,19,50, 48]
print(bubble_sort(testarr))

setArr = [6, 3, 4, 5, 6, 1, 7, 2, 5, 3, 2, 1, 3]

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    # create set from arr
    count_set = set(arr)
    sorted_arr = []

    # built dictionary from set, init to 1
    count_dic = {}
    for item in count_set:
        if item < 0:
            return "Error, negative numbers not allowed in Count Sort"
        else:
            count_dic[item] = 0

    for item in arr:      
        count_dic[item] += 1 

    for k, v in count_dic.items():
        while v > 0:
            sorted_arr.append(k)
            v -= 1

    arr = sorted_arr
    return arr

print(f'COUNT SORT ')
print(count_sort(setArr))    