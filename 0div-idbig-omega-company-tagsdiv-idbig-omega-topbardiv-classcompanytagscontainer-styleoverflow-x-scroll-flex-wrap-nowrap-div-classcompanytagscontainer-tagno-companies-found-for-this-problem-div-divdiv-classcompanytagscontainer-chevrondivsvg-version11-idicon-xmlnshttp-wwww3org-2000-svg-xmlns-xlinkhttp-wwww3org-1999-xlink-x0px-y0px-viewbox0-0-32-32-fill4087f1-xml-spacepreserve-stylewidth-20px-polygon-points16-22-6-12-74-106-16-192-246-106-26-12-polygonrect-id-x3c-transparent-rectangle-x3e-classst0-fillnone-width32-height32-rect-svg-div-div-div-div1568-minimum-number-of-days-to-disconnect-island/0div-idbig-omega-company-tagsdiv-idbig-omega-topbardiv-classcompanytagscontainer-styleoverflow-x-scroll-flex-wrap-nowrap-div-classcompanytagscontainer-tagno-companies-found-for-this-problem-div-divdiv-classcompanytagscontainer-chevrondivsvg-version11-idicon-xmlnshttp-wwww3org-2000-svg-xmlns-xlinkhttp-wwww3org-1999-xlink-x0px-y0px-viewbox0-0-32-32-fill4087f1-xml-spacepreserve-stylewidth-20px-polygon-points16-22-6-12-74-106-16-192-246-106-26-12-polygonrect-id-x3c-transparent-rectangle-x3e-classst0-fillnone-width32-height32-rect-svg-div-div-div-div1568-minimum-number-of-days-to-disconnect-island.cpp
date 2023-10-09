class Solution {
public:
    vector<int> dx={-1,0,1,0};
    vector<int> dy={0,-1,0,1};
    void dfs(int x, int y,   vector<vector<int>> & vis,   vector<vector<int>> &grid){
        int n = grid.size();
        int m = grid[0].size();

        vis[x][y]=1;
        
        for (int a=0;a<4;a++){
            int nx = x+dx[a];
            int ny = y+dy[a];
            
            if (0<=nx and nx<n and 0<=ny and ny<m and !vis[nx][ny] and grid[nx][ny]){
                dfs(nx,ny,vis,grid);
            }
        }
    }
    
    int cntIslands(vector<vector<int>> & grid){
        int islands =0;
        int n= grid.size();
        int m= grid[0].size();
        
        vector<vector<int>> vis(n,vector<int> (m,0));
        
        for (int i=0;i<n;i++)
        {
            for (int j=0;j<m;j++)
            {
                if (!vis[i][j] and grid[i][j])
                {
                    dfs(i,j,vis,grid);
                    islands++;
                }
            }
        }
        return islands;
    }
    
    int minDays(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        
        int num_islands = cntIslands(grid);
        //check for 0 ans
        if (num_islands>1 || num_islands==0)
        {
            return 0;
        }
        else
        {   // check for 1 ans
            for (int i=0; i<n; i++)
            {
                for (int j=0;j<m;j++)
                {
                    if (grid[i][j])
                    {
                        grid[i][j]=0;
                        num_islands = cntIslands(grid);
                        grid[i][j]=1;
                    
                        if (num_islands>1 or num_islands==0) 
                            return 1;
                    }
                }
            }
        }
        return 2;
    
        
    }
};