class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque()
        q.append((beginWord,1))
        
        
        wordSet = set(wordList)
        
        while q:
            ref,t = q.popleft()
            if ref == endWord:
                return t
            for i in range(len(ref)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new = ref[:i]+c+ref[i+1:]
                    if new in wordSet:
                        q.append((new,t+1))
                        wordSet.discard(new)
                        
        return 0