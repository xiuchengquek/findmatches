



## best case =  O(mn)

demul = [{'a','b','c'}, {'c','a'}] * 5
columns = ['a','a','a','b','c'] * 10000




for x in columns:
    print([y for y in demul if x in y])



