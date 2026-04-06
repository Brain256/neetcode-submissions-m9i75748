class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int sum = 0; 

        int min_sum; 
        int min_index = 0; 

        for(int i = 0; i < k; ++i) {
            sum += abs(arr[i] - x); 
            min_sum = sum; 
        }

        for(int i = k; i < arr.size(); ++i) {
            sum += abs(arr[i] - x); 
            sum -= abs(arr[i - k] - x); 

            if(sum < min_sum) {
                min_index = i - k + 1; 
                min_sum = sum; 
            }
        }

        vector<int> res; 

        for(int i = min_index; i < min_index + k; ++i) {
            res.push_back(arr[i]); 
        }

        return res; 
    }
};