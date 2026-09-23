class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=i+1
        achieve =0
        while i<len(prices) and j<len(prices):
            if prices[i]>prices[j] :
                print(prices[i]>prices[j])
                i =j
                j =i+1
                print(i)
            if j< len(prices) and achieve < prices[j] - prices[i] :
                print(i,j)
                achieve= prices[j] - prices[i]
                print('max ',achieve)
            j+=1
        print(achieve)
        return   achieve