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


