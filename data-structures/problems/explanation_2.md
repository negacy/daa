Problem 2: file recursion

A recusive approach is used for this problem. There is a for loop to print all the files in the current path. And, for all subdirectories, a recusive call is  made. The total time complexity is quadratice because O(n), where n is number of files, for the first foor loop, and we are doing recursive call for all subdirectories, which will be O(m-1), where m is number of subdirectories. The total complexity comes to O(n)*O(m-1), which is quadratic. 
