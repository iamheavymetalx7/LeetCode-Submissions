class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
            dic={}
            dic[0]=1    ##before the start 
            ans=0
            summ=0
            for i in range(len(nums)):
                summ+=nums[i]
                summ=summ%k
                if summ in dic:
                    ans+=dic[summ]
                    dic[summ]+=1
                else:
                    dic[summ]=1+dic.get(summ,0)
            return ans
            