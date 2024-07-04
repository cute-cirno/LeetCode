import sys

class UnionFindSet:
    def __init__(self, n):
        self.fa = list(range(n))
    
    def find(self, x):
        if x != self.fa[x]:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]
    
    def union(self, x, y):
        x_fa = self.find(x)
        y_fa = self.find(y)
        if x_fa != y_fa:
            self.fa[y_fa] = x_fa

def get_min_dp(relations, n):
    min_dp = float('inf')
    city = []

    for i in range(1, n + 1):
        ufs = UnionFindSet(n + 1)

        for x, y in relations:
            if x == i or y == i:
                continue
            ufs.union(x, y)

        cnts = [0] * (n + 1)
        for j in range(1, n + 1):
            fa = ufs.find(j)
            cnts[fa] += 1

        dp = max(cnts)
        if dp < min_dp:
            min_dp = dp
            city = [i]
        elif dp == min_dp:
            city.append(i)

    city.sort()
    return " ".join(map(str, city))

if __name__ == "__main__":
    n = int(input())
    relations = []
    for _ in range(n-1):
        relations.append(list(map(int, input().split())))
    result = get_min_dp(relations, n)
    print(result)
