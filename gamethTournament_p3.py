import os
import sys
import importlib  
sys.path.append('strat')


def gamet(u,v):
	mod1=importlib.import_module(strats[u])
	mod2=importlib.import_module(strats[v])
	[p1,p2]=[0,0]
	for _ in range(100):
		h1=[]
		h2=[]
		for __ in range(200):
			s1=mod1.decision(h1,h2)
			s2=mod2.decision(h2,h1)
			if s1<=0.5:
				s1=0
			else:
				s1=1
			if s2<=0.5:
				s2=0
			else:
				s2=1
			h1.append(s1)
			h2.append(s2)
			p1+=U[s1][s2]
			p2+=U[s2][s1]
	return [p1,p2]			

def tournm(S):
	for i in range(len(S)):
		for j in range(i+1,len(S)):
			[p1,p2]=gamet(S[i],S[j])
			results[S[i]]+=p1
			results[S[j]]+=p2

U=[[3,0],[5,1]]

strats=os.listdir("strat")
strats=[x.split('.')[0] for x in strats if x.split('.')[-1]=="py"]
n=len(strats)
results=[0]*n
A=range(n)

tournm(A)

print ('Tournament begins')
for i in A:
	print (strats[i]+'\t'+'\t', results[i])
wA=A[0]
for i in A:
	if results[i] > results[wA]:
		wA=i 
print ('The winner is', strats[wA])

