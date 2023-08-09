class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        
        n,m =len(nums1),len(nums2)
        
        heap =[]
        ans =[]
        seen=set()
        heappush(heap,(nums1[0]+nums2[0],0,0))
        seen.add((0,0))
        
        
        while k and heap:
            val,i,j = heappop(heap)
            
            ans.append([nums1[i],nums2[j]])
            
            if i+1<n and (i+1,j) not in seen:
                heappush(heap,(nums1[i+1]+nums2[j],i+1,j))
                seen.add((i+1,j)) 
            if j+1<m and (i,j+1) not in seen:
                heappush(heap,(nums1[i]+nums2[j+1],i,j+1))
                seen.add((i,j+1))
            
            k-=1
        
        return ans
                
            