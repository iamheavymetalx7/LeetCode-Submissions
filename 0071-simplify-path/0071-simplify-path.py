class Solution:
    def simplifyPath(self, path: str) -> str:
        
        parts=path.split('/')
        # print(parts)
        st=[]
        for p in parts:
            if p in ("","."):
                continue
            elif p=="..":
                if st:
                    st.pop()
            else:
                st.append(p)
        
        return '/'+'/'.join(st)