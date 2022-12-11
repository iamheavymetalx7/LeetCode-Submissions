from heapq import *

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq=[]
        for i in range(min(k,len(nums1))):
            for j in range(min(k,len(nums2))):
                if len(pq)<k:
                    heappush(pq,(-nums1[i]-nums2[j],i,j))
                else:
                    if -nums1[i]-nums2[j]<pq[0][0]:
                        break
                    else:
                        heappop(pq)
                        heappush(pq,(-nums1[i]-nums2[j],i,j))
        result =[]
        for (num,i,j) in pq:
            result.append([nums1[i],nums2[j]])
    
        return result
        