class Solution:
    def twoSum(self, nums, target):
        from collections import defaultdict
        d = defaultdict(int)
        for i, num in enumerate(nums):
            if target-num in d:
                return [d[target-num], i]
            d[num] = i
                
a=Solution()
print(a.twoSum([2, 7, 11, 15],9))
print(a.twoSum([2, 6, 11, 15],9))
print(a.twoSum([],9))
print(a.twoSum([],0))