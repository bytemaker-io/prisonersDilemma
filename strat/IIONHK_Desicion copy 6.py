#Neptun: IIONHK
def decision(h1, h2):
    if len(h2) == 0:
        return 0
    else:
       #tit for tat strategy
        if h2[-1] == 1:
            return 1
        else:
            return 0
