class Solution:
    def fullBloomFlowers(self, flowers, people) -> List[int]:
        flowers.sort()
        sorted_people  = sorted(people)
        
        heap =[]
        i=0
        dic= defaultdict()
        for person in sorted_people:
            while i<len(flowers) and flowers[i][0]<=person:
                heappush(heap,flowers[i][1])
                i+=1
            
            
            while heap and heap[0]<person:
                heappop(heap)
            
            dic[person] = len(heap)
            
            
        ans = [dic[x] for x in people]
        return ans