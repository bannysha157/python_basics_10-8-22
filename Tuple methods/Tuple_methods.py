python Tuple Methods:

Python has two built-in methods that are used for tuples. The following are the two methods:


Method	Description:
  
count()	The tuple.count() method in Python returns the number of times a specified value appears in the tuple.

index()	The tuple.index() method in Python returns the smallest index of the specified element in the tuple.


PROGRAM:  Using count method():

 # initializing the tuple values
 tupleVal = (1, 2, 3,4,5, 7, 8, 7, 5, 5, 6, 4, 4)
 print("Tuple:",tupleVal)
 # counting the number os occureneces of 4 in the given tuple
 occureneces = tupleVal.count(4)
 # printing the returned value
 print("The item '4' occured",occureneces,"times"))

Output:

Tuple: (1, 2, 3, 4, 5, 7, 8, 7, 5, 5, 6, 4, 4)
The item '4' occured 3 times




Example 2:  using indec method():
    
 # initializing the tuple values
 tupleVal = ("e","i","o","u","a","a")
 print("Tuple:",tupleVal)
 # the tuple.index() method
 # finds the first occurrence of the specified value and returns its index
 Index = tupleVal.index("a")
 # printing the returned value
 print("The index value of 'a' is",Index) 

Output:


Tuple: ('e', 'i', 'o', 'u', 'a', 'a')
The index value of  'a' is 4
