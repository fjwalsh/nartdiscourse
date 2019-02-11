#discourse.py

import random

#names
file=open('characters.txt','r')
names=file.readlines()
file.close

#scenarios
file=open('scenarios.txt','r')
scenarios=file.readlines()
file.close

scenario1=random.choice(scenarios)
s=list(scenario1)

for i in range(len(s)):
	if s[i]=='!':
		s[i]=random.choice(names)[:-1]

scenario=''.join(s)

print scenario
