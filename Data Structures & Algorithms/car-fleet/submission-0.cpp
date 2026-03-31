class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int, int>> fleet; 

        for(int i = 0; i < position.size(); ++i) {
            pair<int, int> p = make_pair(position[i], speed[i]); 
            fleet.push_back(p); 
        }

        sort(fleet.rbegin(), fleet.rend()); 

        stack<double> s; 

        for(pair<int, int> car : fleet) {
            double time = (double)(target - car.first) / (double)(car.second); 
            if(s.empty()) {
                s.push(time); 
            }

            if(s.top() < time) {
                s.push(time); 
            }
        }

        return s.size(); 
    }
};
