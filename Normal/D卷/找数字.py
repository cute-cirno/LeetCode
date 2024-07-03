import sys

def get_next_binary_number(n):
    n_bin_str = "0" + bin(n)[2:]
    m_bin_char_arr = list(n_bin_str)

    count_one = 0

    for i in range(len(m_bin_char_arr) - 2, -1, -1):
        if m_bin_char_arr[i] == "0" and m_bin_char_arr[i + 1] == "1":
            m_bin_char_arr[i] = "1"
            m_bin_char_arr[i + 1] = "0"

            if count_one > 0:
                for j in range(i + 2, len(m_bin_char_arr)):
                    if j < len(m_bin_char_arr) - count_one:
                        m_bin_char_arr[j] = "0"
                    else:
                        m_bin_char_arr[j] = "1"
            break

        if m_bin_char_arr[i + 1] == "1":
            count_one += 1

    return int("".join(m_bin_char_arr), 2)

if __name__ == "__main__":
    input = sys.stdin.read().strip()
    n = int(input)
    print(get_next_binary_number(n))
