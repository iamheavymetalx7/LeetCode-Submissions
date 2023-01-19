from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic=defaultdict(list)
        summ=0
        for i,num in enumerate(nums):
            summ+=num
            dic[summ%k].append(i)
        dic[0].append(-1)
        ans=0
        for val,lis in dic.items():
            if len(lis)>1:
                ans+=len(lis)*(len(lis)-1)//2
        
        return ans  