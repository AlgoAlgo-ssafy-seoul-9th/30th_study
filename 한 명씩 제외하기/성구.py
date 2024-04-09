input = __import__("sys").stdin.readline
from collections import deque
N, K = map(int, input().split())

que = deque(range(1, N+1))
i = 1
while que:
    tmp = que.popleft()
    if i % K:
        que.append(tmp)
    else:
        print(tmp, end=" ")
    i += 1