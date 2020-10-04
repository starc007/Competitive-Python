import itertools

def convert_to_path(perm):
    perm = list(perm)
    perm = [0] + perm + [-1]
    path = list()
    for i in range(1, len(perm)):
        path.append((perm[i - 1], perm[i]))
    return path

def solution(times, times_limit):
    rows = len(times)
    bunnies = rows - 2

    for k in range(rows):
        for i in range(rows):
            for j in range(rows):
                if times[i][j] > times[i][k] + times[k][j]:
                    times[i][j] = times[i][k] + times[k][j]

    for r in range(rows):
        if times[r][r] < 0:
            return [i for i in range(bunnies)]

    for i in reversed(range(bunnies + 1)):
        for perm in itertools.permutations(range(1, bunnies + 1), i):
            total_time = 0
            path = convert_to_path(perm)
            for start, end in path:
                total_time += times[start][end]
            if total_time <= times_limit:
                return sorted(list(i - 1 for i in perm))
    return None


print(solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))    