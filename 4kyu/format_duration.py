def format_duration(seconds):
    pass

def minutes(seconds):
    x = 1
    y = 0
    
    while y <= seconds:
        x += 1
        y = x * 60
    
    if x > 60:
        z = x - 60
        print(f"{z} hours and ")
        

print(minutes(3662))