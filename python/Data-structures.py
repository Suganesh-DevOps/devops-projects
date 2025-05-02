
--data structure--
List 
   1. ordered
   2. Mutable
   3. Hetrogenius data types(int, string, float)

common operations:
1. to create a List
   list = []
   list = [1, "sugu", 3.0]
   lsit = list(range(10))

2. How to access using Index
   to access using Index
   mylist[0]
   mylist[-1]
   mylist[1:3]

3. Options to modify list
   mylist[2] = 2 --> index position and value
   mylist.append("New") -> To append at the end.
   mylist.insert(2, 'x') --> to insert x in index 2
   mylist.extend({5, 6}) --> to add to list

4. for removal
   mylist.pop() --> remove the last item in the list
   mylist.pop(2) --> Remove the value at index 2
   mylist.remove(3)  --> remove the value in the 1st occerunce
   del mylist[0:2] --> It is to give range to delete

5. other methods 
   length = len(my_list)
   sorted_list = sorted(my_list)  
   my_list.sort()          
   my_list.reverse()       
   index = my_list.index(True) 
   count = my_list.count(2) 
   words = string.split()  --> Split string into list	