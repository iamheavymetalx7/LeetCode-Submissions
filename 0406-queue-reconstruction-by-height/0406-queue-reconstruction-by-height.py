'''
1. larry stream
2. https://leetcode.com/problems/queue-reconstruction-by-height/discuss/89359/Explanation-of-the-neat-Sort%2BInsert-solution
'''

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ## sort based on max height, and min k -> the number of people front of it
        people.sort(key=lambda p:(-p[0],p[1]))
        
        # print(people)
        
        queue= []
        for p in people:
            queue.insert(p[1],p)
            # print(queue)
        return queue