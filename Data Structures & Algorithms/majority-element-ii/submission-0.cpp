class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        vector<int> mElements; 

        unordered_map<int, int> elements; 

        for(int i = 0; i < nums.size(); ++i) {
            if(elements[nums[i]] == -1) continue; 

            elements[nums[i]]++; 

            if(elements[nums[i]] > nums.size() / 3) {
                elements[nums[i]] = -1; 
                mElements.push_back(nums[i]); 
            }
        }

        return mElements;
    }
};