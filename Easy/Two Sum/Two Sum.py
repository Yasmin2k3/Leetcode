class Solution(object):
    nums = [2, 7, 11, 15]
    target = 9

    def twoSum(nums, target):
        # target = 9 for now; check if the first index is less than nine, check if second
        # index added with first index is greater or less than nine, repeat for all indexes.
        # If that doesnt work, then check if second index is less than nine and continue.

        finalSum = 0

        for i in range(0, len(nums)):
            checker = nums[i]
            if checker == target:
                return 'This number does not work'
            else:
                if checker < target:
                    finalSum += checker
                    break

    twoSum(nums, target)