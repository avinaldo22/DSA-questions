
def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    # def search_item(start, end, arr, target):
    #     for i in range(start, end):
    #         if arr[i] == target:
    #             return i
    #     return -1

    # breakpoint = 0

    # length = len(nums)

    # if length == 1:
    #     if target == nums[0]:
    #         return 0


    # for i in range(length-1):
    #     if nums[i+1]<nums[i]:
    #         breakpoint = i+1
    #         break
    # print(breakpoint)

    # if target > nums[-1] and target >= nums[0]:
    #     return search_item(0, breakpoint, nums, target)
    # elif target <= nums[-1] and target >= nums[breakpoint]:
    #     return search_item(breakpoint, length, nums, target)
    # else:
    #     return -1

    if target in nums:
        return nums.index(target)
    else:
        return -1
        

    