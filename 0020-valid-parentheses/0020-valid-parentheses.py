class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in range(len(s)):
            # print(st)
            if s[i]=="(" or s[i]=="{" or s[i]=="[":
                st.append(s[i])
            if s[i]==")" and not st:
                return False
            if s[i]=="}" and not st:
                return False
            if s[i]=="]" and not st:
                return False
            if s[i]==")" and st[-1]=="(":
                st.pop()
                continue
            if s[i]=="}" and st[-1]=="{":
                st.pop()
                continue
            if s[i]=="]" and st[-1]=="[":
                st.pop()
                continue
            if s[i]==")" and st[-1]!="(":
                st.append(")")
            if s[i]=="}" and st[-1]!="{":
                st.append("}")
            if s[i]=="]" and st[-1]!="[":
                st.append("]")
        return len(st)==0
                
