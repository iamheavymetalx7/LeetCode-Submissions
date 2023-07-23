class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        l=0
        r=max(ranks)*cars*cars+2
        
        
        def check(mid):
            rep=0
            for x in ranks:
                rep += int((mid//x)**(0.5))
            if rep>=cars:
                return True
            
            return False
            
        
        while r>l+1:
            
            
            mid= (l+r)//2
            if check(mid):
                r=mid
            else:
                l=mid
            
        return r