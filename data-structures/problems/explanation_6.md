Problem 6: union and intersection of two lists

To find union of two linked lists, I am depending on an array. First, I add elements of the first linked list to the array. Second, I check if elements of the second linked list are in the array or not. If they are not in the array, the elements are added otherwise ignored. 

The complexity of this algorithm is quadratic because for each element in the second linked list, there is a python `in` operation, which is O(n) by itself, to check if they already exits in the list or not. Adding elements from the first linked list to the array is linear. Also, there is a third operation that reads elements from the array to a linked list, which contains the union. This is also linear. 
