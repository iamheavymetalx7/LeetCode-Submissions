'''
https://leetcode.com/problems/best-sightseeing-pair/discuss/1468367/Code-walk-through-O(n)-time-%2B-O(1)-space
'''

class Solution:
    def maxScoreSightseeingPair(self, a: List[int]) -> int:
        maxLeft = a[0]+0
        maxScore =0
        n=len(a)
        
        
        for i in range(1,n):
            maxScore = max(maxScore, maxLeft+a[i]-i)
            maxLeft = max(maxLeft,a[i]+i)
        return maxScore