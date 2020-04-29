A = [1,5,432,432,235,53,353,13,3]

for i in range(len(A)):
    min_index = i
    for j in range(i+1, len(A)):
        if A[min_index] > A[j]:
            min_index = j
    #swapping
    A[i], A[min_index] = A[min_index], A[i]

for i in range(len(A)):
    print("%d"%A[i], end=", ")
