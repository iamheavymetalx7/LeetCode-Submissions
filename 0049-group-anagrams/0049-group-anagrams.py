from collections import defaultdict

'''
note that if we sort each element in strs, on avg it taks n*logn time to sort.

then to do it for the whole array its of the order (M*NlogN)

A better approach is to use hashmap, where we use counter as a key, counter denotes the count of each alphabet in a word.
By doing, so the time complexity can be reduced to O(M*N)
'''
class Solution: ##going by the first approach of sorting
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        
        for i in range(len(strs)):
            st = ''.join(sorted(strs[i]))
            
            if st in dic:
                dic[st].append(strs[i])
            else:
                dic[st]=[strs[i]]
        ans=[]
        for i,j in dic.items():
            ans.append(j)
        return ans
            
        
        
        