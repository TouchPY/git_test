#两种方法求斐波那契数列

#method1
def feibonaqi(n):
    if n==1 or n==2:
        return 1
    else:
        return feibonaqi(n-1)+feibonaqi(n-2)
fb=feibonaqi(8)
print(fb)
#1 1 2 3 5 8 13 21 34 55 ...

#method2
def fbnq2(n):
    a, b = 1, 1
    if n==1 or n==2:
        return 1
    else:
        for i in range(n-2):
            c=a+b
            a=b
            b=c
        return b
fb2=fbnq2(6)
print(fb2)