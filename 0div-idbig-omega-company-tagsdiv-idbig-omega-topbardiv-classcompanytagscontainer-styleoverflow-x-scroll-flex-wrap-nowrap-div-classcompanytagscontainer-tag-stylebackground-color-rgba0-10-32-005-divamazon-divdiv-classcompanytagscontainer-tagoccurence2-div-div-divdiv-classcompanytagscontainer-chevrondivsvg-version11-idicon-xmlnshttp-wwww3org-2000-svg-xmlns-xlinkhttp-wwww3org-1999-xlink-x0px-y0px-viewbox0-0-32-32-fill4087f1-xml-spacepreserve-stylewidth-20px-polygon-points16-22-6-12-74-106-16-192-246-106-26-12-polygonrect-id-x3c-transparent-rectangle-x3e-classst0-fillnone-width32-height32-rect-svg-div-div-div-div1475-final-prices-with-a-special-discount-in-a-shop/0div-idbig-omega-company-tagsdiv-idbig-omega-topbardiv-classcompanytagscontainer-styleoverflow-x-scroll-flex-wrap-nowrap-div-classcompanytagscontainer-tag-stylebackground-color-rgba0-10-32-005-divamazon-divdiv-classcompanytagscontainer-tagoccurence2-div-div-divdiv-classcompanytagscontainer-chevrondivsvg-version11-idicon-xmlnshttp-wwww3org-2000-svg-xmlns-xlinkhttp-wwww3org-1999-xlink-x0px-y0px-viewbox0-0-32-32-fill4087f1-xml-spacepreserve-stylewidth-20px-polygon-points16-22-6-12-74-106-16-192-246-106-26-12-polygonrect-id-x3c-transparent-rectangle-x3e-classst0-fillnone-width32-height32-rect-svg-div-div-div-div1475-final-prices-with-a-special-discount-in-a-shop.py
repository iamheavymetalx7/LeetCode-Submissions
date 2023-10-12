class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n=len(prices)
        next_smaller = [n for _ in range(n)]
        
        st=[]
        
        for i in range(n):
        
            while st and prices[st[-1]]>=prices[i]:
                top = st.pop()
                next_smaller[top]=i
            st.append(i)
        
        new_prices = prices[:]
        
        for i in range(n):
            if next_smaller[i]==n:continue
            new_prices[i] = new_prices[i] - prices[next_smaller[i]]
        return new_prices
                
            
            