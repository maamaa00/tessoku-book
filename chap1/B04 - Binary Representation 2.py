n = input()

ans = 0
for i in range(len(n)):
    keta = int(n[i])
    kurai = 2 ** (len(n) - 1 - i) 

    ans +=  keta * kurai
    
print(ans)