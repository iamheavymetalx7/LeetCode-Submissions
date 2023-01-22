class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        if s==target:
            return True
        
        # 0 XOR 0 = 0
        # 0 XOR 1 = 1
        # 1 XOR 0 = 1
        # 1 XOR 1 =0
        # We need atleast one '1' in both target and s
        
        
        return ('1' in s)==('1' in target)