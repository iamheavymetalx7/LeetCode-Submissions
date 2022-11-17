'''
Approach 1:
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        for i in zip(*strs):
            p="".join(i)
            
            if len(set(p))!=1:
                return ans
            else:
                ans+=p[0]
        return ans
           

##testcase = ["flower","flow","flight"]

##each 'i' looks like:
##('f', 'f', 'f')
##('l', 'l', 'l')
##('o', 'o', 'i')


##<p, len(set(p))>
##fff 1
##lll 1
##ooi 2
##wwg 2

'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        maxi=max(strs)
        mini=min(strs)
        
        #the maxi and mini gives the lexiographically larget and smallests strings respectively
        for i in range(len(mini)):
            if mini[i]!=maxi[i]:
                return mini[:i]
        return mini  
        