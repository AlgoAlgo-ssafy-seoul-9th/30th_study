import sys, heapq
from collections import defaultdict
input = sys.stdin.readline


def main():
    N = int(input())    
    maxv = 0

    lines = sorted(list(tuple(map(int, input().split())) for _ in range(N)), key=lambda x:x[0])
    
    start, end = -100000001,-100000001
    for s, e in lines:
        if e < start or s > end:
            pass
        else:
            pass



if __name__ == "__main__":
    main()