class Solution:
    '''
    1. https://leetcode.com/problems/the-number-of-beautiful-subsets/discuss/3314183/Python-Backtracking
    2. take / not-take approach
    3.https://leetcode.com/problems/the-number-of-beautiful-subsets/discuss/3314233/Python-Backtracking
    4. cp mohan : good idea of generating all subsets using bitmasking
    '''
    
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n=len(nums)
        s=set()
        res=0
        
        def recur(idx):
            nonlocal res
            if idx>=n:
                return
            for j in range(idx,n):
                if nums[j]+k in s or nums[j]-k in s:
                    continue
                res+=1
                s.add(nums[j])
                recur(j+1)
                s.discard(nums[j])
        recur(0)
        return res  