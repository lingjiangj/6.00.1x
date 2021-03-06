# Exercise: how many

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    
    result = 0
    for key in aDict.keys():
        result += len(aDict[key])
        
    return result
    
    
