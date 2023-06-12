class Solution(object):
    def summaryRanges(self, nums):
        result, n = [], len(nums)
        a = nums[0]

        if n == 0:
            return result

        for i in range(n):
            if (i == n-1) or (nums[i]+1 != nums[i+1]):
                if nums[i] != a:
                    result.append(str(a) + "->" + str(nums[i]))
                else:
                    result.append(str(a))

                if i != n-1:
                    a = nums[i+1]
        return result
