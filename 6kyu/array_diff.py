

def array_diff(a, b):
    """
    remove all values from list a, which are present in list b keeping their order
    array_diff([1,2],[1]) == [2]
    array_diff([1,2,2,2,3],[2]) == [1,3]
    array_diff([1,2,3], [1, 2]) == [3]
    array_diff([1,2,2], [2]) == [1]
    array_diff([1,2,2], [1]) == [2, 2]
    array_diff([1,2,2], []) == [1, 2, 2]
    rray_diff([], [1,2]) == []
    """
    new = a
    for i in b:
        for _ in range(len(a)):
            if i in a:
                new.remove(i)
    return new

print(array_diff([1,2,2], [2]))