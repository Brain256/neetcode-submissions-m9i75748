class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counts; 

        for(int i = 0; i < nums.size(); ++i) {
            counts[nums[i]]++; 
        }

        map<int, vector<int>, greater<int>> frequencies; 

        for(auto obj : counts) {
            frequencies[obj.second].push_back(obj.first); 
        }

        vector<int> result; 
        int total = 0; 

        for(auto obj : frequencies) {
            for(int i = 0; i < obj.second.size(); ++i) {
                if(total == k) {
                    return result; 
                }

                result.push_back(obj.second[i]); 
                ++total; 
            }
            
            if(total == k) {
                return result; 
            }
        }

        return result; 

    }
};
