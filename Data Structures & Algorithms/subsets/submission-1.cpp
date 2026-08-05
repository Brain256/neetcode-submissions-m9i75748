class Solution {
public:
    vector<vector<int>> helper(vector<int>& vec, vector<vector<int>>& res) {
        if (vec.size() == 0) {
            res.push_back({}); 

            return res; 
        }

        int val = vec.back(); 

        vec.pop_back(); 
        int size = res.size(); 

        res.push_back({val}); 

        for(int i = 0; i < size; ++i) {
            vector<int> cur = res[i]; 
            cur.push_back(val); 
            res.push_back(cur); 
        }

        return helper(vec, res); 
    }


    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> temp; 
        return helper(nums, temp); 

    }
};
