class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        mini  =200
        for ele in strs:
            mini=min(mini, len(ele))
            
        j=0
        ans=""
        while j<mini:
            for ele in strs:
                if ele[j]!=strs[0][j]:
                    return ans
            ans+=strs[0][j]
            j+=1
        
        return ans
                    