def main():
    data = input().split()
    
    dataSize = int(data[0])
    datas = list(map(int, data[1:dataSize + 1]))
    
    matrixSize = int(data[dataSize + 1])
    secrets = []
    
    starts = []
    
    index = dataSize + 2
    for i in range(matrixSize):
        secrets.append(list(map(int, data[index:index + matrixSize])))
        for j in range(matrixSize):
            if secrets[i][j] == datas[0]:
                starts.append((i, j))
        index += matrixSize
    
    offsets = [
        (-1, 0),
        (0, -1),
        (0, 1),
        (1, 0)
    ]
    
    def dfs(x, y, index, path, used):
        if index == dataSize:
            return True
        
        for offsetX, offsetY in offsets:
            newX, newY = x + offsetX, y + offsetY
            
            if (
                newX < 0 or newX >= matrixSize or
                newY < 0 or newY >= matrixSize or
                used[newX][newY] or
                secrets[newX][newY] != datas[index]
            ):
                continue
            
            path.append((newX, newY))
            used[newX][newY] = True
            
            if dfs(newX, newY, index + 1, path, used):
                return True
            
            used[newX][newY] = False
            path.pop()
        
        return False
    
    def get_result():
        used = [[False] * matrixSize for _ in range(matrixSize)]
        for x, y in starts:
            used[x][y] = True
            path = [(x, y)]
            if dfs(x, y, 1, path, used):
                return " ".join(f"{x} {y}" for x, y in path)
        
        return "error"
    
    print(get_result())

if __name__ == "__main__":
    main()
