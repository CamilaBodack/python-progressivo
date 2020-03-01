'''
function to compare two arrays positions and return values that increments when a value[i] is greater
'''

def compareTriplets(a, b):
    alice = 0
    bob = 0
    
    for i in range(len(a)):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
        
    return alice, bob

  

    
