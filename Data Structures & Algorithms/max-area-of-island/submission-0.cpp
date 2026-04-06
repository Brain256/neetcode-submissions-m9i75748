class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        vector<vector<int>> visited(grid.size(), vector<int>(grid[0].size(), 0)); 

        queue<pair<int, int>> q; 
        int max_size = 0; 

        for(int i = 0; i < grid.size(); ++i) {
            for(int x = 0; x < grid[i].size(); ++x) {
                int size = 0; 

                if(!visited[i][x] && grid[i][x] == 1) {
                    visited[i][x] = 1; 
                    size = 1; 
                    q.push(make_pair(i, x)); 
                    vector<vector<int>> checks = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}}; 

                    while(!q.empty()) {
                        int first = q.front().first; 
                        int second = q.front().second; 

                        q.pop(); 
                        for(vector<int> check : checks) {
                            int r = first + check[0]; 
                            int c = second + check[1]; 

                            if(r >= 0 && r < grid.size() && c >= 0 && c < grid[i].size()) {
                                if(grid[r][c] == 1) {
                                    if(!visited[r][c]) {
                                        q.push(make_pair(r, c)); 
                                        visited[r][c] = 1; 
                                        size++; 
                                    }
                                }
                            }
                        }
                    }

                    max_size = max(max_size, size); 
                }
            }
        }

        return max_size; 
    }
};
