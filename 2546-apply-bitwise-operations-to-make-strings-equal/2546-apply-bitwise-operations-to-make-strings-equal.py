class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        if s==target:
            return True
        
        return ('1' in s)==('1' in target)