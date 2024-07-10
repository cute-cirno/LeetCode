def get_result(n, s):
    chars = list(s)
    limit = chr(ord('a') + n - 1)
    back = False

    for i in range(len(chars) - 1, -1, -1):
        if chars[i] < limit:
            if not back:
                chars[i] = chr(ord(chars[i]) + 1)
            else:
                back = False

            if i - 1 >= 0 and chars[i] == chars[i - 1]:
                continue
            if i - 2 >= 0 and chars[i] == chars[i - 2]:
                continue

            return ''.join(chars)
        else:
            chars[i] = 'a'
            back = True

    return "NO"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    s = data[1]

    print(get_result(n, s))

if __name__ == "__main__":
    main()
