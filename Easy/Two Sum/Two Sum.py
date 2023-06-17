class Solution(object):
    nums = [3,3]
    target = 6

    def twoSum(self, nums, target):
        finalSum = 0

        for i in range(len(nums)):

            for a in range(i, len(nums)):
                if nums[a] == target:
                    return "This number does not work"
                elif nums[a] < target:
                    finalSum += nums[a]
                    break

            for checker in range(len(nums)):
                if checker == a:
                    pass
                elif nums[checker] == target:
                    return "This number does not work"
                elif nums[checker] + finalSum == target:
                    finalSum += nums[checker]
                    break

            if finalSum == target:
                break
            elif nums[i] != nums[-1]:
                finalSum = 0
            else:
                return "This number does not work"

        return finalSum
