def decision(h1,h2):
    if len(h2)==0:
        return 0
    #从第10次开始，判断对手是不是在模仿我的行为
    if len(h2)==199:
        if h2[-1]==h1[-1] and h2[-2]==h1[-2] and h2[-3]==h1[-3] and h2[-4]==h1[-4] and h2[-5]==h1[-5] and h2[-6]==h1[-6] and h2[-7]==h1[-7] and h2[-8]==h1[-8] and h2[-9]==h1[-9] and h2[-10]==h1[-10]:
            return 1
        else:
            return h2[-1]
    else:
        if h2[-1]==1:
            return 1
        else:
            return 0 
    
    