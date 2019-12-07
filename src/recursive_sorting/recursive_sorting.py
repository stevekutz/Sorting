# TO-DO: complete the helper function below to merge 2 sorted arrays         # fixed typo   helpe >> helper
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements   # cool, inits arr to [0, 0]
    # TO-DO
    # starting at beginning of `arrA` and `arrB`
    # compare the next value of each
    # add smallest to `merged_arr`
    
    # indices for subarrays
    a_index = 0
    b_index = 0    

    # loop through elements
    for i in range(0, elements):
        # check first to prevent index out of range error
        if a_index >= len(arrA): # ArrA is is correct position we incremented to get this condition
            merged_arr[i] = arrB[b_index] # finish up with last position
            b_index += 1
        elif b_index >= len(arrB): # ArrB is done we incremented to get this condition
            merged_arr[i] = arrA[a_index] # finish up with last position
            a_index += 1
        # originally started here, index out of range can occur    
        elif arrA[a_index] < arrB[b_index]:
            merged_arr[i] = arrA[a_index]  # Left elem IS smaller, put into merged_arr
            a_index += 1    # duh, incrmement !!
        # if arrA[a_index] > arrB[b_index]:   NOOO!, cause index out of range
        else:
            merged_arr[i] = arrB[b_index]  # Right elem IS larger, put into merged_arr 
            b_index += 1   

    return merged_arr

# global count
count = 1

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
        # recursively call merge_sort() on LHS
        # recursively call merge_sort() on RHS
        # merge sorted pieces
    global count
    
    if len(arr) > 1:
        leftArr = merge_sort(arr[0: len(arr) // 2]) # pass in lower half split [1, 5, 8, 4, 2], then [1, 5]
        rightArr = merge_sort(arr[len(arr)//2 :])   # pass in upper half split [1,5] >> [5], next we get [8,4,2]
        arr = merge(leftArr, rightArr)    # when we are down to 1 elem, leftArr = 1 & rightArr = 5 passed as args to merge from original left [1,5]
        print(f' pass {count} array is {arr}')
        count += 1

    return arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge_sort(arr1))

# 







# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r): 
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr
