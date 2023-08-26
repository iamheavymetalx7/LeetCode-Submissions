'''
this greedy approach of sorting pairs based on the second element and then greedily picking pairs whenever we can starting from the first pair will always give the length of the longest chain.
'''
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x:x[1])
        
        cnt=0
        curr=-int(1e19)
        
        for pair in pairs:
            if pair[0]>curr:
                cnt+=1
                curr=pair[1]
        return cnt