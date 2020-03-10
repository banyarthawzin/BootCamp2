#Sets

Set&Dictionaries.py
set - {}

include a data type for sets.
Curly brace or the set() function can be use to create sets.

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # show that duplicates have been removed
 
'orange' in basket		# fast membership testing
'crabgrass' in basket


Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a 			# unique letters in a
a - b 		# letters in a but not in b
a | b 		# letters in a or b or both
a & b 		# letters in both a and b
a ^ b 		# letters in a or b but not both

fruits.add("")
fruits.update("")
fruits.remove("")
fruits.discard("")
