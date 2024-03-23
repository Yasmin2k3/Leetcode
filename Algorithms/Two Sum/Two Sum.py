class Solution(object):
    def twoSum(nums, target):
        h = []
        for n in range(len(nums)):
            for c in range(n+1, len(nums)):
                if target - nums[n] == nums[c]:
                    h.append(n)
                    h.append(c)

        return h