# You are given the following definitions:

# A run of monotonically increasing numbers means that a number at position k+1 in the sequence is greater than or equal to the number at position k in the sequence.
# A run of monotonically decreasing numbers means that a number at position k+1 in the sequence is less than or equal to the number at position k in the sequence.
# Implement a function that meets the specifications below.


def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    inc_count = 0 
    dec_count = 0
    maxlen = 0
    result = []
    
    for i in range(len(L)-1):
        if L[i]<=L[i+1]:
            inc_count +=1
            
            if inc_count > maxlen:
                maxlen = inc_count
                result = L[i+1-maxlen:i+1+1]
        else:
            inc_count = 0
        
        if L[i]>=L[i+1]:
            dec_count +=1
            
            if dec_count >maxlen:
                maxlen = dec_count
                result = L[i+1-maxlen:i+1+1]
        else:
            dec_count = 0
        
    return sum(result)
            

    
    
    
