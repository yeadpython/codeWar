def is_square(n):    
    """
    -1  =>  false
    0  =>  true
    3  =>  false
    4  =>  true
    25  =>  true
    26  =>  false
    """
    if n < 0:
        return False
    elif n == 0:
        return True
    else:
        x = 0
        while x * x <= n:
            if x * x == n:
                return True
            x += 1
        return False 

n = int(input("give the number "))
print(is_square(n))