'''
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st=[]
        seen=set()
        i=0
        j=0


        while len(popped)>0:
            # print(st,popped)
            if not st:
                st.append(pushed[i])
                seen.add(pushed[i])
                i+=1
            while st[-1]!=popped[0] and popped[0] not in seen:
                st.append(pushed[i])
                seen.add(pushed[i])
                i+=1

            if st[-1]!=popped[0] and st[-1] in seen:
                return False

            if st[-1]==popped[0]:
                st.pop()
                popped.pop(0)
        return True
'''

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st=[]
        i=0
        
        for ele in pushed:
            st.append(ele)
            
            while len(st)>0 and st[-1]==popped[i]:
                i+=1
                st.pop()
        return True if len(st)==0 else False