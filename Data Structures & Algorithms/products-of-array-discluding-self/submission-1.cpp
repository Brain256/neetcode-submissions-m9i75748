class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> prefix; 
        vector<int> postfix; 
        vector<int> result; 


        int pre = 1; 
        for(int i = 0; i < nums.size(); ++i) {
            pre *= nums[i]; 
            prefix.push_back(pre); 
        }

        int post = 1; 
        for(int i = nums.size()-1; i >= 0; --i) {
            post *= nums[i]; 
            postfix.push_back(post); 
        }

        for(int i = 0; i < nums.size(); ++i) {
            if(i == 0) {
                result.push_back(postfix[nums.size()-2]); 
            } else if(i == nums.size()-1) {
                result.push_back(prefix[i-1]); 
            } else {
                result.push_back(prefix[i-1] * postfix[nums.size()-i-2]); 
            }
        }

        return result; 


    }
};
