class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        cnt=0
        for i in range(1,2001):
            if i in arr:
                continue
            else:
                cnt+=1
                if cnt==k:
                    return i
        