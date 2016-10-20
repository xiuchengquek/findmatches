

## With sort =base case (m + m +n ) , wrose case ( mlogm mn )
## without sour base case ( m + n ) , worse case(  mn )
## might be faster if you sort
## See https://en.wikipedia.org/w/index.php?title=Rabin%E2%80%93Karp_string_search_algorithm&redirect=no ? maybe haha



columns = ['a','a','a','b','c'] * 10000
demul = [{'a','b','c'}, {'c','a'}] * 5

#columns.sort()
previous_x = ''

for ix,x  in enumerate(columns) :

	if x != previous_x:
		current_value = [ s for s in demul if x in s ]

	print(current_value)
	previous_x = x


