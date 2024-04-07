import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

people = deque([i for i in range(1, N+1)])

for i in range(N-K):
    people.appendleft(people.pop())
ans = []
while True:
    ans.append(people.pop())
    if not people:
        break
    for _ in range(K):
        people.append(people.popleft())

print(*ans)