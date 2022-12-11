class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        
        dic={}
        
        for i in nums:
            dic[i]=dic.get(i*i,0)+1
        print(dic)
        t=max(dic.values())
        
        return t if t>=2 else -1
        