class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) { 
        unordered_map<string, vector<string>> counts; 

        for(int i = 0; i < strs.size(); ++i) {
            vector<int> chars(26, 0); 
            for(int j = 0; j < strs[i].size(); ++j) {
                chars[strs[i][j] - 'a']++; 
            }

            string key = ""; 

            for(int i = 0; i < 26; ++i) {
                key += to_string(chars[i]); 
                key += '-'; 
            }

            counts[key].push_back(strs[i]); 
        }

        vector<vector<string>> anagrams; 

        for(auto object : counts) {
            anagrams.push_back(object.second); 
        }

        return anagrams; 
    }
};
