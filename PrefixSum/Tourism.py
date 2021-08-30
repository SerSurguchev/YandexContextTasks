def tourism(points, tracks):
    prefixes_rises_ltr = [0] + [None] * (len(points) - 1)
    prefixes_rises_rtl = [None] * (len(points) - 1) + [0]

    for i in range(1, len(points)):
        prefixes_rises_ltr[i] = \
            prefixes_rises_ltr[i - 1] + max(points[i][1] - points[i - 1][1], 0)
        prefixes_rises_rtl[len(points) - i - 1] = \
            prefixes_rises_rtl[len(points) - i] + max(points[len(points) - i - 1][1] - points[len(points) - i][1], 0)

    results = []
    for track in tracks:
        if track[0] < track[1]:
            results.append(prefixes_rises_ltr[track[1] - 1] - prefixes_rises_ltr[track[0] - 1])
        else:
            results.append(prefixes_rises_rtl[track[1] - 1] - prefixes_rises_rtl[track[0] - 1])

    return results

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
m = int(input())
tracks = [tuple(map(int, input().split())) for _ in range(m)]
results = tourism(points, tracks)
for result in results:
    print(result)
