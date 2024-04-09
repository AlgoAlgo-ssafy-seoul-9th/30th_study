# 30th_study

알고리즘 스터디 30주차

<br/>

# 이번주 스터디 문제

<details markdown="1" open>
<summary>접기/펼치기</summary>

<br/>

## [철로](https://www.acmicpc.net/problem/13334)

### [민웅](./철로/민웅.py)

```py
# 13334_철로_railroad
import sys
import heapq
input = sys.stdin.readline

N = int(input())

home_office = []

for _ in range(N):
    h, o = map(int, input().split())
    home_office.append(sorted([h, o]))

d = int(input())

# O(Nlog(N)) -> 정렬에 소요
home_office.sort(key=lambda x: x[1])
ans = 0
check = []
cnt = 0

# O(N) * O(log(k)), k는 heapq의 원소 수, -> 최대 N일수 있음
# 결과적으로 O(Nlog(N))
for i in range(N):
    h, o = home_office[i]
    if o - h > d:
        continue
    while check and check[0][0] < (o - d):
        s, e = heapq.heappop(check)
        cnt -= 1

    heapq.heappush(check, [h, o])
    cnt += 1
    if cnt > ans:
        ans = cnt

print(ans)

# 최종 시간복잡도 : O(Nlog(N)) + O(Nlog(N)) = O(Nlog(N))
```

### [상미](./철로/상미.py)

```py

```

### [성구](./철로/성구.py)

```py
# 13334 철로
import sys, heapq
input = sys.stdin.readline


def main():
    N = int(input())
    # 정렬해서 입력받기
    rails = sorted(list(sorted(list(map(int, input().split()))) for _ in range(N)), key=lambda x:(x[1],x[0]))
    d = int(input())
    start, end = -100000001, -100000001
    maxv = 0
    indexes = []
    for s, e in rails:
        # 범위가 넘어가면 체크할 필요 X
        if e - s > d:
            continue
        
        # 범위 안에 없으면
        if not (start <= s and e <= end):
            # 최댓값 체크
            maxv = max(maxv, len(indexes))
            # 범위 끝 기준 재 선정
            start = e-d
            end = e
            # 시작이 가장 작은 것부터 가져와서 비교
            while indexes:
                # 범위 내에 들어가면 멈춤
                if indexes[0][0] >= start:
                    break
                # 범위 내에 없으면 뺌
                else:
                    heapq.heappop(indexes)
        # 범위 내 값 저장
        heapq.heappush(indexes, (s,e))
    else:
        # 마지막 큐 안에 값들 체크
        maxv = max(maxv, len(indexes))
        
    print(maxv)
    return


if __name__ == "__main__":
    main()

```

### [영준](./철로/영준.py)

```py

```

<br/>

</details>

<br/><br/>

# 지난주 스터디 문제

<details markdown="1">
<summary>접기/펼치기</summary>

## [한 명씩 제외하기](https://www.codetree.ai/problems/remove-person-at-a-time/description)

### [민웅](./한%20명씩%20제외하기/민웅.py)

```py
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
```

### [상미](./한%20명씩%20제외하기/상미.py)

```py

```

### [성구](./한%20명씩%20제외하기/성구.py)

```py
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

```

### [영준](./한%20명씩%20제외하기/영준.py)

```py
'''
5 3
3 1 5 2 4
'''
N, K = map(int, input().split())
ans = [0] * N
cnt = [0] * (N+1)
j = 0
for i in range(N):
    c = 0
    while c<K:
        j = (j+1)%N
        #print(j)
        if cnt[j]==0:
            c += 1
            
            #print(cnt)
    cnt[j] = 1
    ans[i] = j if j!=0 else N
print(*ans)

```

## [코드트리 회의실](https://www.codetree.ai/problems/codetree-meeting-room/description)

### [민웅](./코드트리%20회의실/민웅.py)

```py
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
```

### [상미](./코드트리%20회의실/상미.py)

```py

```

### [성구](./코드트리%20회의실/성구.py)

```py

```

### [영준](./코드트리%20회의실/영준.py)

```py

```

## [가장 행복한 문자열](https://www.codetree.ai/problems/the-happiest-string/description)

### [민웅](./가장%20행복한%20문자열/민웅.py)

```py

```

### [상미](./가장%20행복한%20문자열/상미.py)

```py

```

### [성구](./가장%20행복한%20문자열/성구.py)

```py

```

### [영준](./가장%20행복한%20문자열/영준.py)

```py

```

</details>

<br/><br/>

# 알고리즘 설명

<details markdown="1">
<summary>접기/펼치기</summary>

<br>

## [철로_Sweeping Algorithm](https://coyote.tistory.com/10)

</details>
