def clothes(undershort, shorts):
    i = j = 0
    best_i = 0
    best_j = 0
    best_diff = float('inf')

    while i < len(undershort) and j < len(shorts):
        diff = abs(undershort[i] - shorts[j])
        if diff == 0:
            return [undershort[i], shorts[j]]

        elif diff < best_diff:
            best_diff = diff
            best_i = i
            best_j = j

        if undershort[i] <= shorts[j]:
            i += 1
        else:
            j += 1
    return [undershort[best_i], shorts[best_j]]

if __name__ == '__main__':
    N = int(input())
    lst1 = list(map(int, input().split()))
    M = int(input())
    lst2 = list(map(int, input().split()))

    num1, num2 = clothes(lst1, lst2)
    print(str(num1) + ' ' + str(num2))
