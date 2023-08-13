def is_triangle(a, b, c):
    '''
    @author: Yead
    Implement a function that accepts 3 integer values a, b, c. 
    The function should return true if a triangle 
    can be built with the sides of given length 
    and false in any other case.
    '''
    if a + b > c and a + c > b and b + c > a: 
        return True 
    else: 
        return False
    
is_triangle(1, 2, 2)
