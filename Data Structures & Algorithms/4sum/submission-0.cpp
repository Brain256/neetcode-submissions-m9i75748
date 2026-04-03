class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end()); 
        vector<vector<int>> res; 
        unordered_set<string> stored; 

        if(nums.size() < 4) {
            return {}; 
        }

        for(int i = 0; i < nums.size(); ++i) {
            for(int j = i+1; j < nums.size()-2; ++j) {
                int t = nums[i] + nums[j]; 

                int l = j+1; 
                int r = nums.size()-1; 

                while(l < r) {
                    long sum = t + (long)nums[l] + (long)nums[r]; 

                    if(sum < target) {
                        l++; 
                    } else if(sum > target) {
                        r--; 
                    } else {
                        string key = to_string(nums[i])+"-"+to_string(nums[j])+"-"+to_string(nums[l])+"-"+to_string(nums[r]); 
                        if(!stored.count(key)) {
                            res.push_back({nums[i], nums[j], nums[l], nums[r]}); 
                            stored.insert(key); 
                        }
                        l++; 
                        r--; 
                    }
                }
            }
        }

        return res; 
    }
};