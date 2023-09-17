#Neptun: IIONHK
def decision(h1, h2):
    # Checking if this is the first round. If true, I will choose to cooperate.
    if len(h2) == 0:
        return 0
    # If this is the last round,I will betray him 
    if len(h2) >= 199:
        return 1
    #try to always cooperate with the opponent
    else:
       #tit for tat strategy
        if h2[-1] == 1:
            return 1
        else:
            return 0
