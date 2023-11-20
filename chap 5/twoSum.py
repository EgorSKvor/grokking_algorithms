# using hash tables time O(n)

# def twoSum(self, nums, target):
#     prevMap = {}
#     for idx, num in enumerate(nums):
#         diff = target - nums[idx]
#         if diff in prevMap:
#             return [prevMap[diff], idx]
#         else:
#             prevMap[num] = idx
#     return


# with time O(n**2)

# def twoSum(nums, target):
#     output = []
#     for i in range(len(nums)):
#         sub_target = target - nums[i]
#         new_arr = nums[i+1:]
#         print(new_arr)
#         for j in range(len(new_arr)):
#             if sub_target == new_arr[j]:
#                 first_ind = i
#                 sec_ind = first_ind + j+1
#                 output.append(first_ind)
#                 output.append(sec_ind)
#                 break
#     return output


# nums = [2, 7, 11, 15]
# target = 17
# print(twoSum(nums, target))
