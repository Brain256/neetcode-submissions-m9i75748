class Solution {
public:
    void dfs(vector<vector<int>>& res, vector<int>& subset, vector<int>& c, int i, int remaining) {
        if (remaining == 0) {
            res.push_back(subset); 
            return;
        } else if (remaining < 0 || i >= c.size()) {
            return;
        }

        subset.push_back(c[i]); 
        dfs(res, subset, c, i, remaining - c[i]); 

        subset.pop_back();
        dfs(res, subset, c, i+1, remaining);  
        
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> s;  
        dfs(res, s, candidates, 0, target); 

        return res; 
    }
};
