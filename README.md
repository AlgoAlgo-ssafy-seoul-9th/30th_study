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

```

### [상미](./한%20명씩%20제외하기/상미.py)

```py

```

### [성구](./한%20명씩%20제외하기/성구.py)

```py


```

### [영준](./한%20명씩%20제외하기/영준.py)

```py


```

## [코드트리 회의실](https://www.codetree.ai/problems/codetree-meeting-room/description)

### [민웅](./코드트리%20회의실/민웅.py)

```py

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



</details>
