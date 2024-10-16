import heapq

def k_largest_elements(nums: list, k: int) -> list:

    ### What we do is we heapify the current array and find out the largest element

    # Implementing using PRIORITY QUEUE
    pq = []

    heapq.heapify(pq)

    for i in range(len(nums)):

        heapq.heappush(pq, nums[i])

        # If size of the priority queue exceeds k stop

        if len(pq) > k:
            heapq.heappop(pq)

    return pq


# Given array
arr = [11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45]
# Size of array
n = len(arr)
k = 3
large_elements = k_largest_elements(arr, k)

print(large_elements)