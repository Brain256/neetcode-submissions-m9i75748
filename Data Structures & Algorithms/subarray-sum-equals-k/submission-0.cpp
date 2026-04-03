class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> prefix_map; 

        int count = 0; 

        int prefix = nums[0];
        prefix_map[nums[0]]++;  

        if(prefix == k) count++; 

        for(int i = 1; i < nums.size(); ++i) {
            prefix += nums[i]; 

            if(prefix == k) count++; 
            if(prefix_map[prefix - k]) count += prefix_map[prefix - k]; 

            prefix_map[prefix]++; 
        }

        return count; 
    }
};