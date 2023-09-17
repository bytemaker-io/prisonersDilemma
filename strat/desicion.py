#Neptun: IIONHK

def decision(h1, h2):
    # Checking if this is the first round. If true, I will choose to cooperate.
    if len(h2) == 0:
        return 0
    
    # If the length of h2 is 199, and check if the opponent is imitating me .If true, I will betray him on the last round.
    if len(h2) == 199:
        # Check if the last 10 elements of h2 are equal to the last 10 elements of h1
        if h2[-1] == h1[-1] and h2[-2] == h1[-2] and h2[-3] == h1[-3] and h2[-4] == h1[-4] and h2[-5] == h1[-5] and h2[-6] == h1[-6] and h2[-7] == h1[-7] and h2[-8] == h1[-8] and h2[-9] == h1[-9] and h2[-10] == h1[-10]:
            # If they are equal, return 1
            return 1
        else:
            # If they are not equal, return the value of the last element of h2
            return h2[-1]
        
    #try to always cooperate with the opponent
    else:
       #tit for tat strategy
        if h2[-1] == 1:
            return 1
        else:
            return 0
