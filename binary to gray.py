def binary_to_gray(n):
    if not(n):
        return 0
    
    a=n%10
    b=int(n/10)%10
    

    if(a and not(b)) or (not(a) and b):
        return(1+10*binary_to_gray(int(n/10)))
    else:
        return (10*binary_to_gray(int(n/10)))


n=int(input())
print(binary_to_gray(n),end='')
