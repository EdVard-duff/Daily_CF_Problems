
def solve() -> None:
    n, m = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(m)]    
    indices = [[0] * (n + 1) for _ in range(m)]
    for i, lst in enumerate(data):
        for j, val in enumerate(lst):
            indices[i][val] = j

    res = left = 0
    while left < n:
        ptrs = [indices[j][data[0][left]] for j in range(m)]
        i = left
        while all(ptr + 1 < n and data[j][ptr + 1] == data[0][ptrs[0] + 1] for j, ptr in enumerate(ptrs)):
            ptrs = [ptr + 1 for ptr in ptrs]
            i += 1
        res += (i - left + 1) * (i - left + 2) // 2
        left += 1
    print(res)

if __name__ == "__main__":
    solve()
