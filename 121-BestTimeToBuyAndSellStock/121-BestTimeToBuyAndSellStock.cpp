// Last updated: 6/12/2025, 8:28:11 PM
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit=0;
        int minvalue=INT_MAX;
        for(int i=0;i<prices.size();i++)
        {
           
                minvalue=min(prices[i],minvalue);
                profit=max(prices[i]-minvalue,profit);
            
        }
       return profit;
        
    }
};