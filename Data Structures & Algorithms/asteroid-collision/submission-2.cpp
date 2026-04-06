class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        stack<int> objects; 
        vector<int> result; 

        for(int i = 0; i < asteroids.size(); ++i) {
            if(asteroids[i] > 0) {
                objects.push(asteroids[i]);

            } else if(!objects.empty()) {
                
                int top = objects.top(); 
                
                while(top <= abs(asteroids[i])) {
                    objects.pop(); 

                    if(top == abs(asteroids[i])) {
                        break; 
                    }

                    if(objects.empty()) {
                        result.push_back(asteroids[i]); 
                        break; 
                    }

                    top = objects.top(); 
                }

            } else {
                result.push_back(asteroids[i]); 
            }
        }

        vector<int> temp; 

        while(!objects.empty()) {
            temp.push_back(objects.top()); 
            objects.pop(); 
        }

        for(int i = temp.size()-1; i >= 0; --i) {
            result.push_back(temp[i]); 
        }

        return result; 
    }
};