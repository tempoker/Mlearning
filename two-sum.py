
import pickle as pkl 
#class Solution(object):
def twoSum(nums, target):
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
    else :
        return False
        # no special case handling becasue it's assumed that it has only one solution


la = [2,5,9,11,6,12]
target = 18
# with open(r'tsum.pkl','wb') as f:
#     pkl.dump(twoSum,f)
with open(r'tsum.pkl','rb') as f:
    twoSum = pkl.load(f)
res = twoSum(la,target)
print(res) #[1,3]
