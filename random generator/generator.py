import random

file=open('characters.txt','r')
names=file.readlines()
file.close

type=raw_input('how many names?')

print random.sample(names, int(type))