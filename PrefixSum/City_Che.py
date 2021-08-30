def Masha(dist, limit):
    count = 0
    right = 1
    for i in dist:
        while right < len(dist) and dist[right] - i <= limit:
            right += 1
        else:
            count += len(dist) - right

    return count

def launch():
    numAndLimit = list(map(int, input().split()))
    distances = list(map(int, input().split()))
    print(Masha(distances, numAndLimit[1]))

if __name__ == '__main__':
    launch()
