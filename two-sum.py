class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            d[num] = i
        # no special case handling becasue it's assumed that it has only one solution
            
la = [2,5,9,11,6,12]
target = 8
a = Solution().twoSum(la,target)
print(a) #[1,3]