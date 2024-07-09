import sys
from collections import defaultdict, deque

def main():
    input = sys.stdin.read
    data = input().strip().split(" ")
    
    relations = [s.split("->") for s in data]
    
    in_degree = defaultdict(int)
    next_tasks = defaultdict(list)
    
    for a, b in relations:
        in_degree[b] += 0
        in_degree[a] += 1
        next_tasks[b].append(a)
    
    queue = deque(sorted([task for task, degree in in_degree.items() if degree == 0]))
    ans = []
    
    while queue:
        new_queue = deque()
        for fa in queue:
            ans.append(fa)
            
            for ch in next_tasks[fa]:
                in_degree[ch] -= 1
                if in_degree[ch] == 0:
                    new_queue.append(ch)
        
        queue = new_queue
    
    print(" ".join(ans))

if __name__ == "__main__":
    main()
