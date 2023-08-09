class Solution:
        
    def ksmallestPairs(self,nums1,nums2,k=200):
        n = len(nums1)
        m=len(nums2)
        
        heap =[]
        
        seen=set()
        res =[]
        heappush(heap,(nums1[0]+nums2[0],0,0))
        seen.add((0,0))
        
        while k and heap:
            val,i,j = heappop(heap)
            res.append(val)
            
            if i+1<n and (i+1,j) not in seen:
                heappush(heap,(nums1[i+1]+nums2[j],i+1,j))
                seen.add((i+1,j))
            
            if j+1<m and (i,j+1) not in seen:
                heappush(heap,(nums1[i]+nums2[j+1],i,j+1))
                seen.add((i,j+1))
            
            k-=1
            
        return res
            
            
        
    def kthSmallest(self, mat: List[List[int]], kk: int) -> int:
        
        mm = len(mat)
        
        res = mat[0]
        
        for i in range(1,mm):
            res = self.ksmallestPairs(res,mat[i])
        
        return res[kk-1]
        
        
