'''
bcab


bca

'''

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        last_occ = defaultdict(int)

        mask = 0
        for i,x in enumerate(s):
            last_occ[x]=i
        
        st =[]
        
        for i,x in enumerate(s):
            val = ord(x)-ord('a')
            if mask&(1<<val)==0:
                while st and st[-1]>x and last_occ[st[-1]]>i:
                    char = st.pop()
                    new_val = ord(char)-ord('a')
                    mask^=(1<<new_val)
                st.append(x)
                mask^=(1<<val)

                
        return ''.join(st)
            
            
        
            
        