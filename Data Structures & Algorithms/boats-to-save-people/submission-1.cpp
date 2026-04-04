class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end()); 

        int n = people.size(); 
        int boats = 0; 
        int l = 0; 
        int r = n-1; 

        while(l <= r) {

            if(l == r) {
                boats++; 
                break; 
            }; 

            int total_weight = people[l] + people[r]; 

            if(total_weight > limit) {
                boats++; 
                r--; 
            } else {
                boats++; 
                r--; 
                l++; 
            }
        }

        return boats; 
    }
};