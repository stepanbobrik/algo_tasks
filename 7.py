def getSimple(n):
    prime = [1]*(n+1)
    prime[0]= prime[1] = 0
    for i in range(2,n+1):
        if prime[i]:
            if i*i <= n:
                j = i *i
                while j <= n:
                    prime[j] = 0
                    j+=i
    ans= []
    for i in range(len(prime)):
        if prime[i]:
            ans.append(i)
    return ans
