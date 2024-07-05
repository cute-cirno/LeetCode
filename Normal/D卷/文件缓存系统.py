class Node:
    def __init__(self, key, val, freq):
        self.key = key
        self.val = val
        self.freq = freq
        self.prev = None
        self.next = None

class Link:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def add_last(self, node):
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1

    def remove(self, node):
        if self.size == 0:
            return

        if self.size == 1:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail == node:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        self.size -= 1

class LFUCache:
    def __init__(self, capacity):
        self.key_map = {}
        self.freq_map = {}
        self.capacity = capacity
        self.min_freq = 0

    def get(self, key):
        if key not in self.key_map:
            return
        node = self.key_map[key]
        self.inc_node_freq(node)

    def put(self, key, val):
        if self.key_map.get(key):
            return

        while self.capacity < val:
            if self.min_freq == 0:
                return

            min_freq_link = self.freq_map[self.min_freq]
            remove_node = min_freq_link.head
            self.capacity += remove_node.val
            min_freq_link.remove(remove_node)
            del self.key_map[remove_node.key]

            if min_freq_link.size == 0:
                del self.freq_map[self.min_freq]

                if self.freq_map:
                    self.min_freq = min(self.freq_map.keys())
                else:
                    self.min_freq = 0

        self.capacity -= val
        self.min_freq = 1
        node = Node(key, val, self.min_freq)

        if self.min_freq not in self.freq_map:
            self.freq_map[self.min_freq] = Link()

        self.freq_map[self.min_freq].add_last(node)
        self.key_map[key] = node

    def inc_node_freq(self, node):
        link = self.freq_map[node.freq]
        link.remove(node)

        if link.size == 0:
            del self.freq_map[node.freq]

            if node.freq == self.min_freq:
                self.min_freq += 1

        node.freq += 1

        if node.freq not in self.freq_map:
            self.freq_map[node.freq] = Link()

        self.freq_map[node.freq].add_last(node)


def main():
    data = input().split()
    m = int(data[0])
    lfu_cache = LFUCache(m)

    n = int(data[1])
    index = 2
    for _ in range(n):
        operation = data[index]
        file_name = data[index + 1]

        if operation == "put":
            file_size = int(data[index + 2])
            lfu_cache.put(file_name, file_size)
            index += 3
        else:
            lfu_cache.get(file_name)
            index += 2

    if lfu_cache.capacity == m:
        print("NONE")
    else:
        print(",".join(sorted(lfu_cache.key_map.keys())))

if __name__ == "__main__":
    main()
