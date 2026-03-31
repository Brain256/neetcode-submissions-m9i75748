class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char, int> chars_s1; 

        for(int i = 0; i < s1.size(); ++i) {
            chars_s1[s1[i]]++; 

        }

        unordered_map<char, int> chars_s2; 
        int window_size = s1.size(); 
        
        for(int i = 0; i < window_size; ++i) {
            chars_s2[s2[i]]++; 
        }

        for(int i = window_size; i < s2.size(); ++i) {
            if(chars_s1 == chars_s2) {
                return true; 
            }

            chars_s2[s2[i]]++; 

            chars_s2[s2[i-window_size]]--; 

            if(chars_s2[s2[i-window_size]] == 0) {
                chars_s2.erase(s2[i-window_size]); 
            }
        }

        return chars_s1 == chars_s2; 
    }
};
