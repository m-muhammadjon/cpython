def get_grids(grid):
    l = len(grid)
    s = 3
    out = [[None]*l for _ in range(l)]
    for n in range(l):
        for m in range(l):
            k = (n // s) * s + m // s
            j = (n % s) * s + m % s
            out[k][j] = grid[n][m]
    return out
mat = []
for i in range(9):
    nums = list(map(int, input().split()))
    mat.append(nums)
for i in mat:
    if len(set(i)) != 9:
        print(i)
        print('No')
        exit()

for i in get_grids(mat):
    if len(set(i)) != 9:
        print(i)
        print('No')
        exit()
# print(mat)
for i in range(9):
    xd = []
    for j in range(9):
        xd.append(mat[i][j])
    print(xd)
    if len(set(xd)) != 9:
        print(xd)
        print('No')
        exit()
print('Yes')


