class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cm = Counter(moves)
        
        flag = True
        
        if cm["U"]!=cm["D"]:
            flag=False
        
        if cm["L"]!=cm["R"]:
            flag=False
            
        if flag:
            return flag
        
        return flag
            
        
        