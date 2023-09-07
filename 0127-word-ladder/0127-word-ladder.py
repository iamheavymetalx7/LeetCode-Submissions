class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        q=deque()
        q.append((beginWord,0))
        
        chars = 'abcdefghijklmnopqrstuvwxyz'

        
        wordSet = set(wordList)
        vis=set()
        while q:
            ref,t = q.popleft()
            if ref == endWord:
                return t+1
            
            for i in range(len(ref)):
                for c in chars:
                    new = ref[:i]+c+ref[i+1:]
                    
                    if new in wordSet:
                        wordSet.discard(new)
                        q.append((new,t+1))
                
        return 0
                    
                    