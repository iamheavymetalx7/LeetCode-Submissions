from collections import Counter
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        arr=[]
        for key in c.keys():
            arr.append(key)
        
        arr.sort()
        
        new_sorted = []
        for ele in arr:
            new_sorted.extend([ele]*c[ele])
        
        return new_sorted
            
        