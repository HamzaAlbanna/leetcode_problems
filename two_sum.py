class Solution(object):
    def twoSum(self, nums, target):
        ln = len(nums)
        for i in range(ln):
            for g in range(i + 1, ln):
                ss = nums[i] + nums[g]
                if ss == target:
                    return [i, g]# return the index not the numbers --> [nums[i], nums[g]]
ret = Solution().twoSum([2,7,11,15], 9)
print(ret)