class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for(int i = 0; i < board.size(); ++i) {
            unordered_set<char> seen; 
            for(int j = 0; j < board[i].size(); ++j) {
                if(board[i][j] == '.') continue; 

                if(seen.count(board[i][j])) {
                    return false; 
                }

                seen.insert(board[i][j]); 
            }
        }

        for(int i = 0; i < board.size(); ++i) {
            unordered_set<char> seen; 
            for(int j = 0; j < board[i].size(); ++j) {
                if(board[j][i] == '.') continue; 

                if(seen.count(board[j][i])) {
                    return false; 
                }

                seen.insert(board[j][i]); 
            }
        }

        for(int i = 0; i < 3; ++i) { 
            for(int j = 0; j < 3; ++j) {
                unordered_set<char> seen;
                for (int k = 0; k < 3; ++k) {
                    for(int x = 0; x < 3; ++x) {
                        int r = i * 3 + k; 
                        int c = j * 3 + x; 

                        if(board[r][c] == '.') continue; 

                        if(seen.count(board[r][c])) {
                            return false; 
                        }

                        seen.insert(board[r][c]); 
                    }  
                }
                
            }
        }

        return true; 
    }
};
