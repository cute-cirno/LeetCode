R = int(input())
N = list(map(int, input().split()))
D = int(input())

def calc_sub(bin1):
    ans = 0
    for i in range(len(bin1)):
        ans += bin1[i] * (1 << i)
    return ans

def binary_sub(minuend, subtrahend):
    i = len(minuend) - 1
    while i >= 0:
        if minuend[i] >= subtrahend[i]:
            minuend[i] -= subtrahend[i]
        else:
            if calc_sub(minuend[0:i + 1]) < calc_sub(subtrahend[0:i + 1]):
                j = i + 1
                while j < len(minuend):
                    if minuend[j] > 0:
                        minuend[j] -= 1
                        return True
                    else:
                        j += 1
                return False
            else:
                minuend[i] -= subtrahend[i]
                minuend[i - 1] += 1
        i -= 1
    return True

def getResult():
    subtrahend = list(map(int, str(bin(D))[2:]))
    subtrahend.reverse()

    count = 0

    for i in range(len(subtrahend), R + 1):
        count += N[i]

    minuend = N[0:len(subtrahend)]
    while len(minuend) < len(subtrahend):
        minuend.append(0)

    while binary_sub(minuend, subtrahend):
        count += 1

    return count

print(getResult())