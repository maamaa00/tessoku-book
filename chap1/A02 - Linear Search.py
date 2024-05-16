n, x = map(int, input().split())
l = list(map(int, input().split()))

ans = 'No'
for i in range(n):
    if x == l[i]:
        ans = 'Yes'
    
print(ans)