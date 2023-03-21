from collections import defaultdict
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        dic=defaultdict(list)
        
        dic[0].append(-1)
        s=0
        for i,j in enumerate(nums):
            s+=abs(j)
            dic[s].append(i)
        ans=0
        print(dic)
        for k,v in dic.items():
            if len(v)>1:
                ans+=((len(v)-1)*(len(v)))//2
        return ans
            
        