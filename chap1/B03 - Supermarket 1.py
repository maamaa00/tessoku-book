n = int(input())
l = list(map(int, input().split()))

ans = 'No'
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if l[i] + l[j] + l[k] == 1000:
                ans = 'Yes'

print(ans)