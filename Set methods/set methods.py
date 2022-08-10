Methods	Description
add()	  The set.add() method adds the specified element to the set

clear()	  The set.add() method in Python removes all the elements from the set.

copy()	  This method returns a Shallow Copy for the Set

difference()	 The set.difference() method in Python returns a set containing the difference between two or more sets

difference_update()	  The difference_update() method in Python removes the common elements from the original set that are also included in another, given set.
discard()	      The set.discard() method in Python removes the specified  element from the Set

intersection()	The set.intersection() method in Python returns a set  that contains the intersection or the common elements between or among the given sets

intersection_update() 	This method removes the elements in this set that are not present in other given set(s).

isdisjoint()	  The set.disjoint() method in Python checks whether the specified sets are disjoint(whether two sets have a intersection) or not.

issubset()	 This method returns a boolean value true is another set that contains this set.

issuperset()	The set.issuperset() method in Python Returns whether this set contains another set or not

pop()	  The set.pop() method removes an arbitrary element from the set.

remove()	  The set.remove() method in python removes the specified item from the set.

symmetric_difference()	   This method returns a set with the symmetric differences of two sets

symmetric_difference_update()     This method Updates the original Set With Symmetric Difference of the given two sets.

union()	   The union() method return a set containing the union of the set(s).

update()	  The set.update() method in Python updates the set with the union of this set and others





=>Removing elements from a set():

A particular item can be removed from a set using the methods discard() and remove().
The only difference between the two is that the discard() function leaves a set unchanged if the element is not present in the set.
On the other hand, the remove() function will raise an error in such a condition (if element is not present in the set).


Difference between discard() and remove():
  
PROGRAM:

# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)
# Output: {1, 3, 5, 6}
# discard an element
my_set.discard(4)
print(my_set)
# Output: {1, 3, 5}
# remove an element
my_set.remove(6)
print(my_set)
# Output: {1, 3, 5}
# discard an element
# not present in my_set
my_set.discard(2)
print(my_set)
# you will get an error.
# Output: KeyError
# remove an element
# not present in my_set
my_set.remove(2)
#output key error

Output:

{1, 3, 4, 5, 6}
{1, 3, 5, 6}
{1, 3, 5}
{1, 3, 5}
Traceback (most recent call last):
  File "<string>", line 28, in <module>
KeyError: 2
  
  
  =>set add(): The add() method adds a given element to a set. If the element is already present, it doesn't add any element.
The syntax of add() method is: set.add(elem)
add() method doesn't add an element to the set if it's already present in it.

Also, you don't get back a set if you use add() method when creating a set object.

noneValue = set().add(elem)
The above statement doesn't return a reference to the set but 'None', because the statement returns the return type of add which is None.

Set add() Parameters: add() method takes a single parameter:

elem - the element that is added to the set
Return Value from Set add()
add() method doesn't return any value and returns None.



Example:
  
prime_numbers = {2, 3, 5, 7}
# add 11 to prime_numbers
prime_numbers.add(11)
print(prime_numbers)

# Output: {2, 3, 5, 7, 11}


Example 1: Add an element to a set:
    
# set of vowels
vowels = {'a', 'e', 'i', 'u'}
# adding 'o'
vowels.add('o')
print('Vowels are:', vowels)
# adding 'a' again
vowels.add('a')
print('Vowels are:', vowels)
 
Output:
Vowels are: {'a', 'i', 'o', 'u', 'e'}
Vowels are: {'a', 'i', 'o', 'u', 'e'}
  
  
  Example 2: Add tuple to a set:
      
# set of vowels
vowels = {'a', 'e', 'u'}
# a tuple ('i', 'o')
tup = ('i', 'o')
# adding tuple
vowels.add(tup)
print('Vowels are:', vowels)
# adding same tuple again
vowels.add(tup)
print('Vowels are:', vowels)

Output:

Vowels are: {('i', 'o'), 'e', 'u', 'a'}
Vowels are: {('i', 'o'), 'e', 'u', 'a'}





















