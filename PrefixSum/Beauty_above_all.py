from collections import Counter

def get_coordinates(n, k, number_list):

    number_counter = Counter()
    left = 0
    result = (0,  len(number_list))

    for right, color in enumerate(number_list):
        number_counter[color] += 1
        if len(number_counter) == k:
            while number_counter[number_list[left]] > 1:
                number_counter[number_list[left]] -= 1
                left += 1

            if (result[1] - result[0]) > (right - left):
                result = (left, right)

    return f'{result[0]+1} {result[1]+1}'


if __name__ == '__main__':
	n, k = map(int, input().split())
	number_list = list(map(int, input().split()))
	print(get_coordinates(n, k, number_list))
