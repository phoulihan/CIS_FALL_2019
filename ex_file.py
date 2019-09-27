# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 21:02:14 2019

@author: pathouli
"""

#lecture 1 examples

#variables do not a number != 
a_2 = 'hello'
print (a_2)
a = 1
a*5

#string concatenation
the_str = a_2 + ' ' + 'students'
print (the_str)

the_str_ex = a_2 + str(a)
print (the_str_ex)

my_list = list()
my_list.append(1)
my_list.append(2)
my_list.append('bv')
my_list.append(2)

my_list[0]
my_list[1]
my_list[2]

print (len(my_list))

my_list_ex = [1,2]

#unique storage
the_set = set()
the_set.add(1)
the_set.add(2)
the_set.add('bv')
the_set.add(2)
the_set.add('Bv')
the_set.add('bv')

#dictionary
the_dictionary = {'key_a': 34}
the_keys = the_dictionary.keys()
the_values = the_dictionary.values()
the_dictionary['key_b'] = 45
the_dictionary['key_a'] = 656

#loops
for word in my_list:
    print (word)

for k,v in zip(the_dictionary.keys(),the_dictionary.values()):
    print (k)
    print (v)

#strings
the_string = "the trout jumped up the waterfall into a bears mouth"

for word in the_string:
    print (word)
    
import re

the_new_string = re.sub('bear', 'mountain lion', the_string)

for word in the_string.split():
    print (word)
    
the_string = "the #$%trout jumped!!! up the!!3434 waterfall 43434 into a bears mouth!!!!"
the_new_string = re.sub('[^A-z]+', ' ', the_string)

my_numbers = [1,2,3,4,5,6]

my_num_list = list()
for word in my_numbers:
    my_num_list.append(word%2)

my_num_list_new = [word%2 for word in my_numbers]

