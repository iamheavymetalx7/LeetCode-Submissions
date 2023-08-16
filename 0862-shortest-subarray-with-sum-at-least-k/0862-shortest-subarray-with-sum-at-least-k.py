'''
To slide window, we keep append previous iterated index to a queue as left end and current iterating index as right end. So left end would be q[0] and right end would be i. Once we found psum[i] - psum[q[0]] >= K, we have a valid window. Then we keep reducing window's size by left popping q (increase left end) until window comes to be invalid(psum[i] - psum[q[0]] < k).

Since K >= 1, we don't need to consider decreasing psum elements. For example, if we have psum array = [4,8] and new psum = 2, we just retain [2] and pop out 8 and 4 since 2-8<1 and 2-4<1. 

---> So we can reduce our queue size by maintaining a mono-increasing queue

# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/262641/Python-Prefix-Sum-and-Sliding-Window

# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/143726/C%2B%2BJavaPython-O(N)-Using-Deque

'''

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n=len(nums)
        pref =[0]*(n)
        pref[0]=nums[0]
        for i in range(1,n):
            pref[i]=pref[i-1]+nums[i]
        
        res=int(1e19)
        q=deque() 
        q.append([-1,0]) # idx,val
        for i in range(n):
            cur = pref[i]
                        
            while q and cur-q[0][1]>=k:
                res = min(res,i-q.popleft()[0])
            
            ## we maintain a monotnic inc queue
            while q and cur<=q[-1][1]:
                q.pop()
            
            q.append([i,cur])
        
        if res==int(1e19):
            return -1
        return res
                
            
            
            
            
        
        
        
            