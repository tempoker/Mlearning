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
            
la = [2,5,9,11,6,12,13,14]
target = 8
aa = Solution()
res = aa.twoSum(la,target)
print(res) #[1,3]