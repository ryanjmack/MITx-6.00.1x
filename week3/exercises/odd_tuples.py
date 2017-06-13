def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup, starting with the first element
    '''
    output = ()
    for i in range(0, len(aTup), 2):
        output += aTup[i:i + 1]

    return output
    
