import sys
import collections

def main():
    # 读取输入
    nums = list(map(int, input().split()))
    sorted_nums = list(map(int, input().split()))

    n = len(nums)
    map_num_to_block = [0] * (n + 1)

    for i in range(n):
        num = sorted_nums[i]
        map_num_to_block[num] = i // 3

    queue = collections.deque()
    blocks = collections.defaultdict(list)

    for num in nums:
        block_num = map_num_to_block[num]
        if not queue or queue[-1]['num'] != block_num:
            new_block = {'num': block_num, 'count': 1}
            queue.append(new_block)
            blocks[block_num].append(new_block)
        else:
            queue[-1]['count'] += 1

    moved_count = 0

    while queue:
        first = queue.popleft()
        if first['count'] == 0 or first['count'] == 3:
            continue

        if not queue:
            break

        second = queue[0]
        while second['count'] == 0:
            queue.popleft()
            if not queue:
                break
            second = queue[0]
        if not queue:
            break

        if first['num'] == second['num']:
            second['count'] += first['count']
            continue

        if first['count'] == 2:
            moved_count += 1
            for block in blocks[first['num']]:
                block['count'] = 0
            continue

        if first['count'] == 1:
            if len(blocks[first['num']]) == 3:
                moved_count += 2
                for block in blocks[first['num']]:
                    block['count'] = 0
            else:
                moved_count += 1
                for block in blocks[first['num']]:
                    block['count'] = 3

    print(moved_count)

if __name__ == "__main__":
    main()
