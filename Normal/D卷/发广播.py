class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.count = size
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路径压缩
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX
            self.count -= 1

def calculate_minimum_broadcast_count(matrix):
    size = len(matrix)
    union_find = UnionFind(size)
    for i in range(size):
        for j in range(i + 1, size):
            if matrix[i][j] == '1':
                union_find.union(i, j)
    return union_find.count


# 读取输入，这里默认输入是一行，逗号分隔的多个字符串，每个字符串是由空格分隔的字符
data = input().strip()
matrix = [[c for c in line.strip()]for line in data.split(",")]

# 计算并输出最小广播次数
print(calculate_minimum_broadcast_count(matrix))
