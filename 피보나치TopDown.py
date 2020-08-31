caching = [0] * 100 # Memoization 

def fibo(n):
    if n == 1 or n == 2 :
        return 1
    if caching[n] != 0 :
        return caching[n]
    
    caching[n] = fibo(n-1) + fibo(n-2)
    return caching[n]

print(fibo(99))