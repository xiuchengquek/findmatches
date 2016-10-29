
from collections import defaultdict





demul = [{'a','b','c'}, {'c','a'}] * 5
demul_index = defaultdict(list)


for i,x in enumerate(demul):
	for y in x :
		demul_index[y].append(i)


print(demul_index) ## this will return {a : [1,2] , b: [1], c : [1,2]}

## so now you can do a hash look up :
columns = ['a','a','a','b','c'] * 10000

for lines in columns:
	results = demul_index[lines]
	matches = [demul[x] for x in results ]
	print(matches)

