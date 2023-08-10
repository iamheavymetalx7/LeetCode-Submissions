class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st_nums=[]
        st_expressions= []
        
        q= deque()
        
        for x in tokens:
            q.append(x)
        
        
        while q:
            tk = q.popleft()
            if ((len(tk)>=2 and tk[0]=="-") or (tk.isdigit())):
                st_nums.append(tk)
            
            else:
                b = st_nums.pop()
                a = st_nums.pop()
                a=int(a);b=int(b)
                # print(a,b)
                if tk=="+":
                    st_nums.append(str(b+a))
                elif tk=="/":
                    if a*b<0:
                        a=abs(a)
                        b=abs(b)
                        val = a//b
                        val*=-1
                        st_nums.append(str(val))
                    else:
                        st_nums.append(a//b)
                elif tk=="*":
                    st_nums.append(str(a*b))
                else:
                    st_nums.append(str(a-b))
        return int(st_nums[0])
        
        