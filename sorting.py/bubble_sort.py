def bubble_sort(arr):

    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


#array declaration
array_= [20, 40, 50, 60, 30, 10, 23, 54, 1, 198, 345, 6]
#calling function
bubble_sort(array_)
# test case for function
for i in array_:
    print (i, end=", ")


