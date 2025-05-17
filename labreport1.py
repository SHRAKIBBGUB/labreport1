import random

class Node:
    def __init__(self, x, y, depth):
        self.x = x
        self.y = y
        self.depth = depth

class DFS:
    def __init__(self, N):
        self.N = N
        self.grid = [[random.choice([0, 1]) for _ in range(N)] for _ in range(N)]
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.path = []
        self.top_order = []
        self.found = False
        self.source, self.goal = self.get_valid_positions()
    
    def get_valid_positions(self):
        while True:
            sx, sy, gx, gy = random.randint(0, self.N-1), random.randint(0, self.N-1), random.randint(0, self.N-1), random.randint(0, self.N-1)
            if (sx, sy) != (gx, gy) and self.grid[sx][sy] == 1 and self.grid[gx][gy] == 1:
                return Node(sx, sy, 0), Node(gx, gy, float('inf'))
    
    def dfs(self, x, y, depth):
        if self.found or not (0 <= x < self.N and 0 <= y < self.N) or self.grid[x][y] == 0:
            return
        
        self.grid[x][y] = 0
        self.path.append((x, y))
        self.top_order.append((x, y))
        
        if (x, y) == (self.goal.x, self.goal.y):
            self.found = True
            self.goal.depth = depth
            return
        
        for dx, dy in self.directions:
            self.dfs(x + dx, y + dy, depth + 1)
            if self.found:
                return
    
    def solve(self):
        print("Grid:")
        for row in self.grid:
            print(" ".join(map(str, row)))
        print(f"Source: ({self.source.x}, {self.source.y})")
        print(f"Goal: ({self.goal.x}, {self.goal.y})")
        
        self.dfs(self.source.x, self.source.y, 0)
        
        if self.found:
            print("DFS Path:", " -> ".join(map(str, self.path)))
            print("Topological Order of Traversal:", " -> ".join(map(str, self.top_order)))
            print(f"Moves required: {self.goal.depth}")
        else:
            print("No path found")

if __name__ == "__main__":
    N = random.randint(4, 7)
    dfs_solver = DFS(N)
    dfs_solver.solve()
