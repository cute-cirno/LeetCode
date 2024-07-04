import sys

def main():
    # 读取 m 和 n
    m, n = map(int, input().strip().split())
    
    # 读取 speeds
    speeds = list(map(float, input().strip().split()))
    
    # 计算 arrived
    arrived = max(n / speed + i for i, speed in enumerate(speeds))
    
    # 计算 cost
    cost = arrived - (m - 1)
    
    # 输出结果，保留三位小数
    print(f"{cost:.3f}".rstrip('0').rstrip('.'))

if __name__ == "__main__":
    main()
