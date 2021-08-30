def numbers_sum(k, nums):
    result = 0
    left = 0
    current_sum = 0
    for right, num in enumerate(nums):
        current_sum += num
        while current_sum > k and left <= right:
            current_sum -= nums[left]
            left += 1

        if current_sum == k:
            result += 1

    return result


n, k = map(int, input().split())
nums = list(map(int, input().split()))
print(numbers_sum(k, nums))
