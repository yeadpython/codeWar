# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 15:27:47 2023

@author: Yead
"""

def friend(x):
    '''
    Make a program that filters a list of strings and 
    returns a list with only your friends name in it.
    If a name has exactly 4 letters in it, 
    you can be sure that it has to be a friend of yours! 
    Otherwise, you can be sure he's not...
    
    Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
    '''
    f_list = []
    for i in x:
        if len(i) == 4:
            f_list.append(i)
    
    return f_list
        
    
print(friend(["Ryan", "Kieran", "Mark"]))