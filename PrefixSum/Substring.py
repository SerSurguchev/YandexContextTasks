import math
from collections import defaultdict

def substring(input_str, k):
    best_result = (-math.inf, 0)
    left = 0
    counter = defaultdict(int)
    substring_length = 0
    for right_char in input_str:
        while counter[right_char] >= k:
            counter[input_str[left]] -= 1
            substring_length -= 1
            left += 1

        counter[right_char] += 1
        substring_length += 1
        if substring_length > best_result[0]:
            best_result = (substring_length, left + 1)

    return best_result

def main():
    n, k = map(int, input().split())
    input_str = input()
    print(*substring(input_str, k))

if __name__ == '__main__':
    main()
