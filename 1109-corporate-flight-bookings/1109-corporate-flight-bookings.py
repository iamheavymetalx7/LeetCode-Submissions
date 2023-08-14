class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seats =[0]*(n+1)
        
        for x,y,num in bookings:
            seats[x-1]+=num
            seats[y]-=num
        
        for i in range(1,n+1):
            seats[i]+=seats[i-1]
        
        return seats[:-1]