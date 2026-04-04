class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> seen; 
        int max_count = 0; 
        int max_substr = 0; 
        int l = 0; 
        int r = 0; 

        while(r < s.size()) { 

            seen[s[r]]++;
            max_count = max(max_count, seen[s[r]]);

            if(r - l + 1 - max_count > k) {

                seen[s[l]]--;
                l++;
            }

            max_substr = max(max_substr, r - l + 1);
            r++;
        }

        return max_substr;
    }
};
