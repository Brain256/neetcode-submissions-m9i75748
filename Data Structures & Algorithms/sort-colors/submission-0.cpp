class Solution {
public:
    void sortColors(vector<int>& nums) {
        for(int i = 0; i < nums.size(); ++i) {
            int min_index = i; 
            for(int j = i; j < nums.size(); ++j) {
                if(nums[j] < nums[min_index]) {
                    min_index = j; 
                }
            }

            int temp = nums[i]; 
            nums[i] = nums[min_index];  
            nums[min_index] = temp; 
        }
    }
};