class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        unordered_set<string> seen_triplets; 
        unordered_map<int, int> seen; 
        vector<vector<int>> triplets; 

        for(int i = 0; i < nums.size(); ++i) {
            seen[nums[i]]++;
        }

        for(int i = 0; i < nums.size()-2; ++i) {
            int target = 0 - nums[i];

            seen[nums[i]]--; 

            for(int j = i+1; j < nums.size(); ++j) {
                seen[nums[j]]--; 
                if(seen[target - nums[j]]) {
                    vector<int> triple;
                    triple = {nums[i], nums[j], target - nums[j]}; 
                    sort(triple.begin(), triple.end()); 

                    string key = to_string(triple[0]) + "-" + to_string(triple[1]) + "-" + to_string(triple[2]);

                    if(!seen_triplets.count(key)) {
                        triplets.push_back(triple); 
                        seen_triplets.insert(key); 
                    } 
                } 
                seen[nums[j]]++; 
            } 
        }

        return triplets; 
    }
};
