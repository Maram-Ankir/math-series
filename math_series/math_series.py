def fibonacci(n):
    if n ==0:
        return n
    elif n==1:
        return n 
    else:
        return fibonacci(n-1)+ fibonacci(n-2)



def lucas(n):
    if n ==2:
        return n
    elif n==1:
        return n 
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n,a=0,b=1):
    if a==0 and b==1:
        return fibonacci(n)
    elif a==2 and b==1:
        return lucas(n)
    else:
        print('neither fibonacci nor locas')
        return n 

print(sum_series(4,2,3))