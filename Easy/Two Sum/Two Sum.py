class Solution(object):
    nums = [2, 7, 11, 15]
    target = 22

    def twoSum(nums, target):
        finalSum = 0

        for i in range(len(nums)):

            for a in range(i, len(nums)):
                if nums[a] == target:
                    return "This number does not work"
                elif nums[a] < target:
                    finalSum += nums[a]
                    break

            for checker in nums:
                if checker == finalSum:
                    pass
                elif checker == target:
                    return "This number does not work"
                elif checker + finalSum == target:
                    finalSum += checker
                    break

            if finalSum == target:
                break
            elif nums[i] != nums[-1]:
                finalSum = 0
            else:
                return "This number does not work"

        return finalSum


    print(twoSum(nums, target))
