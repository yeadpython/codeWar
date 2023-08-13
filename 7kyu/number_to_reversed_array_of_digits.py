def digitize(n):
    """
    Given a random non-negative number, 
    you have to return the digits of this 
    number within an array in reverse order.
    
    Example(Input => Output):
    35231 => [1,3,2,5,3]
    0 => [0]
    """
    x = str(n)
    l = []
    
    for i in x[::-1]:
        l.append(int(i))

    return l

    # return map(int, str(n)[::-1]) # one liner
    # return [int(x) for x in str(n)[::-1]] # one liner
    # return [int(x) for x in reversed(str(n))] # one liner

print(digitize(0))
print(digitize(548702838394))