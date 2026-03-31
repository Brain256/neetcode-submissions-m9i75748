class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> seen; 
        int max_count = 0; 

        for(int i = 0; i < nums.size(); ++i) {
            if(!seen.count(nums[i])) {
                seen.insert(nums[i]); 
            } 
        }

        for(int i = 0; i < nums.size(); ++i) {
            if(seen.count(nums[i]-1)) continue; 

            int count = 0; 
            int curNum = nums[i]; 
            while(seen.count(curNum)) {
                ++count; 
                ++curNum; 
            }

            max_count = max(count, max_count); 
        }

        return max_count; 
    }
};
