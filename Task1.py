"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
uniq_numbers = set()
for line in texts:
    a,b, _  = line
    uniq_numbers.add(a)
    uniq_numbers.add(b)

for line in calls:
    a,b,_,_ = line
    uniq_numbers.add(a)
    uniq_numbers.add(b)
print("There are " + str(len(uniq_numbers)) +" different telephone numbers in the records.")
