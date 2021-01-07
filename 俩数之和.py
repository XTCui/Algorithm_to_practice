
'''
俩数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
'''

# arr=[1,3,6,15]
# target=9
# '''
# 一遍哈希表
# '''
# def two_sum_with_dict2(nums, target):
#     _dict = {}
#     for i, e in enumerate(nums):
#         if _dict.get(target - e) is not None:
#             return (_dict.get(target - e), i)
#         _dict[e] = i
#
# res=two_sum_with_dict2(arr,target)
# print(res)
'''
暴力循环
'''

# def twoSum(nums,target):
#     for i, m in enumerate(nums):
#         j=i+1
#         while j<len(nums):
#             if target == m+nums[j]:
#                 return [i,j]
#             else:
#                 j+=1
#
# res = twoSum(arr,target)
# print(res)

