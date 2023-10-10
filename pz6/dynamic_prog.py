def count_ways(n):
    if n<=1:
        return 1
    d=[0]*(n+1)
    d[1]=1
    for i in range(2,n+1):
        d[i]+=d[i-1]
        d[i]+=d[i-2]
        if i%2==0:
            d[i]+=d[i//2]
    return d[n]
n = int(input(('Введите значение n: ')))
result = count_ways(n)
print(f'Кол-во способов достичь {n} из точки 1: {result}')
