class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<unordered_map<char, int>> v; 
        vector<vector<string>> anagrams; 
        for(int i = 0; i < strs.size(); i++) {
            bool found = false; 
            unordered_map<char, int> letters; 

            for(int x = 0; x < strs[i].size(); x++) {
                letters[strs[i][x]]++; 
            }

            for(int x = 0; x < v.size(); x++) {
                if(v[x] == letters) {
                    found = true; 
                    anagrams[x].push_back(strs[i]); 
                } 
            }
            if(!found) {
                anagrams.push_back({strs[i]});
                v.push_back(letters); 
            }
            
                
        }

        return anagrams; 
    }
};
