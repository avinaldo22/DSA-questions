

def reverseArray(arr):
    n = len(arr)

    for i in range(n // 2):
        temp = arr[i]
        arr[i] = arr[n - i - 1]
        arr[n - i - 1] = temp








if __name__ == "__main__":
    arr = [2, 4, 6, 7]

    reverseArray(arr)

    for i in range(len(arr)):
        print(arr[i], end=" ")