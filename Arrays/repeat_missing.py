# def repeatedNumber(A):
    
#     output_list = []
    
#     A = list(A)
    
#     A.sort()
    
#     for i in range(len(A) - 1):
#         if A[i] == A[i+1]:
#             output_list.append(A[i])
#             break
    
#     for i in range(len(A) - 1):
#         if A[i+1] - A[i] > 1:
#             output_list.append(A[i]+1)
    
#     return output_list

# out = repeatedNumber([3,1,2,5,3])

# print(out)

import numpy as np


def repeatedNum(arr):

    n = len(arr)


    Sn = n * (n+1) / 2
    S2n = n*(n+1)*(2*n+1)/6

    S = sum(arr)
    S2 = sum(map(lambda x:x*x, arr))

    val1 = S - Sn
    val2 = (S2 - S2n)/val1

    X = (val1 + val2)/2
    Y = val2 - X 

    return int(X),int(Y)


out = repeatedNum([3,1,2,5,3])

print(out)