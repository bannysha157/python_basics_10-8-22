Methods	Explanation:
  
append ->  The list.append() method adds an item to the end of the list.

extend ->The list.extend() method extends the list by appending all the items from the iterable.

insert -> The list.insert() method adds an element at the specified position

remove -> the list.remove() method removes the first item with the specified value

pop	-> he list.pop() method removes the element at the specified position of the list.

Clear	-> The list.clear() method removes all the elements from the list

Index	-> The list.index() method returns the index of the first element with the given list value.

Count	-> The list.count() method returns the number of times x appears in the list.

Sort ->	This method sorts the items of the list

Reverse	-> This method reverses the elements of the list in place.

Copy -> The list.copy() method returns a copy of the specified list



Example 1 : append():
    

 # list.append() method:
  
 week_list = ["Monday", "Tuesday", "Wednesday","Thursday","Friday", "Saturday"]
 print("List before calling append() method\n", week_list)
 # appending sunday at the end of the list
 week_list.append("Saturday")
 print("List after calling append() method")
 print(week_list)
 #list.extend() method
 str_list = ['The odd number', 'are:'] 
 num_list = [1, 3, 5, 7, 9] 
 str_list.extend(num_list) 
 print ("The extended list:",str_list)
 # list.remove() methods
 num_list.remove(5)
 num_list.remove(9)
 print("After removing the 5,9 values:",num_list) 

Output:

 List before calling append() method
  ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
 List after calling append() method
 ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Saturday']
 The extended list: ['The odd number', 'are:', 1, 3, 5, 7, 9]
 After removing the values: [1, 3, 7] 
  
  
  
  Example 2: using pop():
     
    
 # the list.pop() method
 fruits = ['apple', 'banana', 'cherry']
 print("List: ",fruits)
 #removing the first element from the list
 fruits.pop(1)
 print("After removing the first element ")
 print("List: ",fruits)
 # list.index() method
 # printing the index of 'cherry' in fruits list  
 print("The index value of string value 'cherry': ",fruits.index('cherry'))
 # list.clear() method
 fruits.clear()
 print("After calling the clear() method..")
 print("fruits list:",fruits)
  
Output:
 List:  ['apple', 'banana', 'cherry']
 After removing the first element 
 List:  ['apple', 'cherry']
 The index value of string value 'cherry':  1
 After calling the clear() method..
 fruits list: [] 
    
    
    
    
    
    
    Example 3: sort():
    
  # passing the alphabets list
 alphaList = ['b', 'a', 'e', 'd', 'c']
 print("Actual list: ",alphaList)
 # sort the alphabets list in the ascending order
 alphaList.sort()
 # priningt the list in a sorted order
 print('Sorted list:',alphaList)
 # list.reverse() method
 # reversing the order of the alpha list
 alphaList.reverse()
 print('Reversed list:',alphaList)
 # the list.copy() method
 # copying the the old list
 newList= alphaList.copy()
 print("New List: ", newList) 

Output:
 Actual list:  ['b', 'a', 'e', 'd', 'c']
 Sorted list: ['a', 'b', 'c', 'd', 'e']
 Reversed list: ['e', 'd', 'c', 'b', 'a']
 New List:  ['e', 'd', 'c', 'b', 'a'] 
    
  
  
  
  
  





