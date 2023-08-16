'''
we use lazy remove and two heaps (max heap and min heap in order to find the solution)

we maintain large-small <=1 in terms of size 


Another way to formulate things :

In case x >= large[0][0] (ie we add the new element to large).

If nums[i] < large[0][0] then we need to move one element from large to small to restablish initial lengths (because large just got an element, but we know that small will lose one element soon).

If nums[i] == large[0][0] then it's a bit tricky : we don't know if nums[i] is in small or in large, but the key is we don't care. If nums[i] is actually in small, we need obviously to move one element from large to small. But if nums[i] is in large, then it means the size of small and large are already OKAY, but moving large[0][0] is also fine, large lose nothing, small gain nothing, the "real" lengths remain the same. So it's always okay to move large[0] to small in case nums[i]==large[0][0]

if nums[i] > large[0][0], the element to remove is inside large, but large just received one new element, so we don"t need to do anything : the lengths of small and large are already good.
'''

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        small,large=[],[]
        
        
        
        def move(h1,h2):
            x,i = heappop(h1)
            heappush(h2,(-x,i))
        
        def get_median(h1,h2,k):
            return h2[0][0]/1. if k%2 else (h2[0][0]-h1[0][0])/2.
        
        for i,x in enumerate(nums[:k]):
            heappush(small,(-x,i))
        
        for _ in range(k-k//2):
            move(small,large)

        ans = [get_median(small, large, k)]

        
        for i,x in enumerate(nums[k:]):
            if x >= large[0][0]:
                heapq.heappush(large, (x, i+k))
                if nums[i]<=large[0][0]:
                    move(large, small)
            else:
                heapq.heappush(small, (-x, i+k))
                if nums[i]>=large[0][0]:
                    move(small, large)
                
            while small and small[0][1] <= i: 
                heapq.heappop(small)
            while large and large[0][1] <= i: 
                heapq.heappop(large)
            ans.append(get_median(small, large, k))
        return ans