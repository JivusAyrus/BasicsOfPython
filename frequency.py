from collections import Counter

my_list = ['a','a','b','b','b','c','d','d','d','d','d']
count = Counter(my_list) 

print(count) 

print(count['b']) 

print(count.most_common(1)) # 
