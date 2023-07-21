class Solution:
    def largestVariance(self, s: str) -> int:
        count1 = 0
        count2 = 0
        max_variance = 0
        
        pairs = [(l1, l2) for l1 in set(s) for l2 in set(s) if l1 != l2]

        # run once for original string order, then again for reverse string order
        for runs in range(2):
            for x,y in pairs:
                count1 = count2 = 0
                for c in s:
                    if c!=x and c!=y:
                        continue
                    
                    count1 += c==x
                    count2 += c==y
                    if count1 < count2:
                        count1 = count2 = 0
                    elif count1 > 0 and count2 > 0:
                        max_variance = max(max_variance, count1 - count2)
                
            
            # reverse the string for the second time around
            s = s[::-1]
                
        return max_variance