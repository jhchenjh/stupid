# 23 Jan, 2020
# Runtime: 796 ms, faster than 36.85% of Python online submissions for Two Sum.
# Memory Usage: 12.9 MB, less than 63.01% of Python online submissions for Two Sum.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        ans_dict = {}
        ans_dict[nums[0]] = 0
        for i in range(1, len(nums)):
            ans = target - nums[i]
            if ans not in ans_dict.keys():
                ans_dict[nums[i]] = i
            else:
                result = [ans_dict[ans], i]
                break
        return result
