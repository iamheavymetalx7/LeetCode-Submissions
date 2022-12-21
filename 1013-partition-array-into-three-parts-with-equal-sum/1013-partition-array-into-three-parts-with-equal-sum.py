class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        
        if total%3!=0:
            return False
        
        each_sum = total//3
        
        cnt=0
        summ=0
        for i in range(len(arr)):
            summ+=arr[i]
            if summ==each_sum:
                summ=0
                cnt+=1
            
        if cnt>=3:
            return True
        return False
        