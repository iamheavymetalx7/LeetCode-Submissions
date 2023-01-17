class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        count_ones=0
        
        total_flips =0
        
        for char in s:
            if char=="1":
                count_ones+=1
            else:
                total_flips = min(total_flips+1, count_ones)
        return total_flips
        