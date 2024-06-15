def longest_substring_with_one_letter(s):
    n = len(s)
    max_length = -1
    left = 0
    letter_count = 0
    letter_index = -1
    
    for right in range(n):
        if s[right].isalpha():
            letter_count += 1
            letter_index = right
        
        while letter_count > 1:
            if s[left].isalpha():
                letter_count -= 1
            left += 1
        
        if letter_count == 1:
            if all(c.isdigit() for i, c in enumerate(s[left:right+1]) if i != letter_index - left):
                max_length = max(max_length, right - left + 1)
    
    return max_length

# 示例用法
input_string = "a123b456"
print(longest_substring_with_one_letter(input_string))
