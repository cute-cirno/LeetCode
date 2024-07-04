import sys
import json

def get_result(relations):
    fa = {}
    for f, c in relations:
        if f not in fa:
            fa[f] = []
        fa[f].append(c)
        if c not in fa:
            fa[c] = []

    def get_high_c(f, src, high_c):
        if f == 1:
            return 0
        for c in fa[f]:
            if c < src:
                if c not in high_c:
                    high_c.add(c)
                    get_high_c(c, src, high_c)
            elif c == src:
                return 0
        return len(high_c)

    ans = [[f, get_high_c(f, f, set())] for f in fa]
    ans.sort(key=lambda x: x[0])
    return [arr[1] for arr in ans]

if __name__ == "__main__":
    relations = json.loads(input())
    result = get_result(relations)
    print(result)
