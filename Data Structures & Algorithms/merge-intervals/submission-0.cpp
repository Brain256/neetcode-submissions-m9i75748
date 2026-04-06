class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end()); 
        
        vector<int> interval = {intervals[0][0], intervals[0][1]}; 
        vector<vector<int>> res = {}; 

        for(int i = 1; i < intervals.size(); ++i) {
            if(intervals[i][0] <= interval[1]) {
                interval[1] = max(interval[1], intervals[i][1]); 
            } else {
                res.push_back(interval); 
                interval = {intervals[i][0], intervals[i][1]}; 
            }
        }

        res.push_back(interval); 
        return res; 
    }
};
