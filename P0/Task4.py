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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
def setOfTelemarketers(calls, texts):
    call_orig = [] 
    call_rec = []
    text_orig = []
    text_rec = []

    telemarketers = []

    for line in calls:
        call_orig.append(line[0])
        call_rec.append(line[1])
    for line in texts:
        text_orig.append(line[0])
        text_rec.append(line[1])
    for num in call_orig:
        if num not in call_rec + text_orig + text_rec:
            telemarketers.append(num)
    return set(telemarketers)
print("These numbers could be telemarketers: ")
for num in sorted(setOfTelemarketers(calls, texts)):
    print(num)

