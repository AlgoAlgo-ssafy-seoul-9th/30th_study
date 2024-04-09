import sys
import heapq
from sortedcontainers import SortedSet

input = sys.stdin.readline

def bs(ss, pos):
    l, r = 0, len(ss)-1
    while l <= r:
        mid = (l+r)//2
        if ss[mid] <= pos:
            l = mid+1
        else:
            r = mid-1
    return r


times = []
N, M = map(int, input().split())
meeting_room = SortedSet()

cnt = 0
for _ in range(N):
    s, e = map(int, input().split())
    heapq.heappush(times, [s, e])

while times:
    tmp = heapq.heappop(times)
    # print(tmp)

    if len(meeting_room) < M:
        meeting_room.add(tmp[1])
        cnt += 1
    else:
        idx = bs(meeting_room, tmp[0])
        if idx >= 0:
            rv = meeting_room[idx]
            meeting_room.remove(rv)
            meeting_room.add(tmp[1])
            cnt += 1

print(cnt)