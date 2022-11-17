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
           
'''
testcase = ["flower","flow","flight"]

each 'i' looks like:
('f', 'f', 'f')
('l', 'l', 'l')
('o', 'o', 'i')


<p, len(set(p))>
fff 1
lll 1
ooi 2
wwg 2

'''