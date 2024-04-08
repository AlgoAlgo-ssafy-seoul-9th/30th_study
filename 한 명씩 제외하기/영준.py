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
