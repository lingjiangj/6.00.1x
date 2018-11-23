#Write a function is_triangular that meets the specification below. A triangular number is a number obtained by the continued summation of integers starting from 1. For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, etc., are triangular numbers.

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    my_list = []
    n = 2  
    while True:
        num = sum(range(0,n))
        my_list.append(num)
        n +=1
        if k <= num:
            break
    return k in my_list
    
    
