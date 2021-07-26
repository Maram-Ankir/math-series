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


def sum_series(n , n1=0 , n2=1):
    if(n > 1 and n1==0 and n2==1):
        return fibonacci(n)
    if(n >1 and n1==2 and n2==1):
        return lucas(n)
    else:
     if(n == 0 ):
         return n1
     if(n == 1):
       return n2
     else:    
       return sum_series(n-1 , n1 ,n2) + sum_series(n-2 , n1 ,n2)
print(sum_series(4))

# print(sum_series(4,3,4))