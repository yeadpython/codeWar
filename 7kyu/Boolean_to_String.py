def boolean_to_string(b):
    """a function which convert the given 
    boolean value into its string representation.
    
    boolean_to_string(True) ---> "True"
    boolean_to_string(False) ---> "False"
    """
    if b:
        return "True"
    if not b:
        return "False"
    
    # return str(b)
print(boolean_to_string(True))