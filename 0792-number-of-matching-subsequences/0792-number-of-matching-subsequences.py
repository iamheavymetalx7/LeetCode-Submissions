'''
similar to trie approach done using dictionary
-  https://leetcode.com/problems/number-of-matching-subsequences/discuss/329381/Python-Solution-With-Detailed-Explanation
'''
'''
inally, we only go thru S once, and go thru each letter in each word once, therefore, the time complexity is O(M+N), kind of similar to 2 pointers. The trick here is just to use first letter as dict key and the word as value, this way, each time actually we don't scan all words, but just relevant words. Each such scan is guaranteed to cancel one characters.

However the implementation in this post is having a higher time complexity, since string slicing is linear time.


'''
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        word_dict =defaultdict(list)
        cnt = 0
        
        for word in words:
            word_dict[word[0]].append(word)
        
        
        for char in s:
            start_word_expected = word_dict[char]
            word_dict[char]=[]
            
            for ele in start_word_expected:
                if len(ele)==1:
                    cnt+=1
                else:
                    word_dict[ele[1]].append(ele[1:])
        return cnt