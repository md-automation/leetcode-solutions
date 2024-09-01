class Solution:

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        def dfs(r, c):

            if r < 0 or r >= len(grid2) or c < 0 or c >= len(grid2[0]) or grid2[r][c] == 0:
                return True
            
            if grid1[r][c] == 0:
                self.is_sub_island = False
            
            grid2[r][c] = 0
            
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
            
            return self.is_sub_island
        
        count = 0
        
        for r in range(len(grid2)):

            for c in range(len(grid2[0])):

                if grid2[r][c] == 1:
                    self.is_sub_island = True
                    
                    if dfs(r, c):
                        count += 1
        
        return count