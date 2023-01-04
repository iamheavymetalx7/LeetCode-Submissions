from collections import defaultdict
import math
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        dd=defaultdict(int)
        for i in range(len(tasks)):
            dd[tasks[i]]+=1
        print(dd)
        min_ans=0
        for key in dd.keys():
            if dd[key]==1:
                return (-1)
            else:
                # 7 -> 2-2 3-1
                # 11 -> 3-3 2-1
                # 10 -> 3-2, 2-2
                    
                if dd[key]%3==0:
                    min_ans+=dd[key]//3
                else:
                    while dd[key]>4:
                        dd[key]-=3
                        min_ans+=1
                    min_ans+=dd[key]//2
                
                
                # print(ans1+ans2,ans3+ans4,"combo")
                # min_ans += min(ans1+ans2,ans3+ans4)
        return min_ans
    
                
                