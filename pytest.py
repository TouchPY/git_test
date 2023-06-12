def feibonaqi(n):
    if n==1 or n==2:
        return 1
    else:
        return feibonaqi(n-1)+feibonaqi(n-2)
fb=feibonaqi(8)
print(fb)
#1 1 2 3 5 8 13 21 34 55 ...
