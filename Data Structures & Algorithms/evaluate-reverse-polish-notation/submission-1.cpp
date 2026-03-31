class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> numbers; 

        for(int i = 0; i < tokens.size(); ++i) {

            if(tokens[i] == "+") {
                int first = numbers.top(); 
                numbers.pop(); 
                int second = numbers.top(); 
                numbers.pop(); 

                numbers.push(first + second); 
            } else if(tokens[i] == "-") {
                int first = numbers.top(); 
                numbers.pop(); 
                int second = numbers.top(); 
                numbers.pop(); 

                numbers.push(second - first); 
            } else if(tokens[i] == "*") {

                int first = numbers.top(); 
                numbers.pop(); 
                int second = numbers.top(); 
                numbers.pop(); 

                numbers.push(first * second); 
            } else if(tokens[i] == "/") {
                int first = numbers.top(); 
                numbers.pop(); 
                int second = numbers.top(); 
                numbers.pop(); 

                numbers.push(second / first); 
            } else {
                numbers.push(stoi(tokens[i])); 
            }
        }

        return numbers.top(); 

    }
};
