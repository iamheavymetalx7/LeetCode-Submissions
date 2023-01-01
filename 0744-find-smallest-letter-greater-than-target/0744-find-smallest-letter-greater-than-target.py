class Solution:
    def BinarySearch(self,letters,target):
        low=0
        high=len(letters)-1

        while low<=high:

            mid = (low+high)//2

            if target<letters[mid]:
                high=mid-1
            else:
                low=mid+1
                
        return low%len(letters)
                
        
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        target=ord(target)
        
        letters=[ord(letter) for letter in letters]
        print(letters,target)
        ans = self.BinarySearch(letters,target)
        return chr(letters[ans])