# NEPTUN1 NEPTUN2

import numpy as np

def decision(h1, h2):
	if len(h2)==0:
		r=np.random.randint(2)
		return r
	else:
		avg=1.0*sum(h2)/len(h2)
		if avg<=0.5:
			return 0
		else:
			return 1
