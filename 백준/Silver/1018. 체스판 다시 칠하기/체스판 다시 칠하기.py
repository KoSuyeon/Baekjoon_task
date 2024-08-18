N, M = map(int, input().split()) # 행, 열
chess = [input() for _ in range(N)]

def count_changes(x, y, start_color, chess):
    changes = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:  # 짝수 위치
                if chess[x + i][y + j] != start_color:
                    changes += 1
            else:  # 홀수 위치
                if chess[x + i][y + j] == start_color:
                    changes += 1
    return changes

ans = float('inf')
for i in range(N - 7):
    for j in range(M - 7):
        ans = min(ans, count_changes(i, j, 'B', chess), count_changes(i, j, 'W', chess))

print(ans)