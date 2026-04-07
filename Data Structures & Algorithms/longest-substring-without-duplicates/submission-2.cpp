class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> seen; 

        int l = 0; 
        int r = 0; 
        int max_len = 0; 

        while(r < s.size() && l < s.size()) {
            if(seen[s[r]]) {
                seen[s[l]]--; 
                l++; 
            } else {
                seen[s[r]]++; 
                max_len = max(max_len, r - l + 1); 
                r++;
            }
        }

        return max_len; 
    }
};
