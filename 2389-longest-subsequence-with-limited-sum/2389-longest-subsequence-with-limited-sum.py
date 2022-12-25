class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        
        res=[]
        for q in queries:
            count=0
            value=0
            for num in nums:
                if value+num>q:
                    break
                value+=num
                count+=1
            res.append(count)
        return res
        