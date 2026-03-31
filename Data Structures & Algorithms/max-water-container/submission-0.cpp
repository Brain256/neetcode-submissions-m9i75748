class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0; 
        int r = heights.size()-1; 

        int max_water = 0; 
        
        while(l < r) { 
            int water = min(heights[l], heights[r]) * (r-l); 
            max_water = max(max_water, water); 

            if(heights[l] <= heights[r]) {
                ++l; 
            } else if(heights[l] > heights[r]) {
                --r; 
            }
        }

        return max_water; 


    }
};
