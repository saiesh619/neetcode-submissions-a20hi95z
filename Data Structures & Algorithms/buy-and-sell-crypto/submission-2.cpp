class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int sell  ;
        int buy = 0 ;
        int maxProfit = 0 ;
        int minBuy = INT_MAX ;
        for(sell = 0 ; sell < prices.size() ; sell++){
            minBuy = min(prices[sell],minBuy) ;
            maxProfit = max(maxProfit,prices[sell] - minBuy) ;
        }
        return maxProfit;
    }
};

