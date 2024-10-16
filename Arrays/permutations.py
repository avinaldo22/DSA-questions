# # Expectation Code

# # class Solution(object):
# #     def nextPermutation(self, nums):
# #         """
# #         :type nums: List[int]
# #         :rtype: None Do not return anything, modify nums in-place instead.
# #         """
# #         #find the value right before the last peak (pre-peak value)
# #         #sort everything after that value
# #         #find first value in sorted region that is greater than pre-peak value (first larger)
# #         #swap pre-peak value and first larger

# #         #1520 (5 = 1 is pre-peak value)
# #         #1025 (sorting everything after pre-peak)
# #         #1025 (2 is first larger value in sorted region)
# #         #2015 (swap pre-peak and first larger)

# #         for i in range(len(nums)-1, 0, -1):
# #             if nums[i] > nums[i-1]:
# #                 nums[i:] = sorted(nums[i:])

# #             pre_peak_idx = i-1 #pre-peak-idx

# #             for i in range(i, len(nums)):
# #                 if nums[i] > nums[pre_peak_idx]:
# #                     tmp = nums[i]
# #                     nums[i] = nums[pre_peak_idx]
# #                     nums[pre_peak_idx] = tmp
# #                     return nums
        
# #         return nums.reverse()



# ## MY CODE

# class Solution(object):
#     def nextPermutation(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """


#         length = len(nums)

#         if length <= 1:
#             return nums
        
#         i = length - 2

#         while i >= 0 and nums[i] >= nums[i+1]:
#             i -= 1
        
#         if i>=0:

#             j = length-1
#             while nums[j] <= nums[i]:
#                 j -= 1

#             nums[i], nums[j] = nums[j], nums[i]

#         nums[i+1:] = reversed(nums[i+1:])

#         return nums
