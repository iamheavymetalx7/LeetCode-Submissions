'''
This can be the approach:
https://leetcode.com/problems/mice-and-cheese/discuss/3368256/Python-Heap-or-In-depth-Explanation


We will write a more shorter code here
'''
class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        
        return sum(reward2)+sum(nlargest(k, (a-b for a,b in zip(reward1,reward2))))