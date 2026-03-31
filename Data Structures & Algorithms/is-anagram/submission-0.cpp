class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> s_map; 
        if(t.size() != s.size()) {
            return false;
        }
        for(int i = 0; i < s.size(); i++) {
            if(s_map.find(s[i]) == s_map.end()) {
                s_map[s[i]] = 1; 
            } else {
                s_map[s[i]]++; 
            }
        }

        for(int i = 0; i < t.size(); i++) {
            if(s_map.find(t[i]) == s_map.end()) {
                return false; 
            } else {
                s_map[t[i]]--; 

                if(s_map[t[i]] == 0) {
                    s_map.erase(t[i]); 
                }
            }
        }

        return true; 


    }
};
