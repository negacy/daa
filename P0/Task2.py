"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
duration_of_calls = {}
for line in calls:
    calling, receiving, time, duration = line
    if time.split()[0].endswith('09-2016'):#specific to September 2016.
        if calling not in duration_of_calls.keys():
            duration_of_calls[calling] = int(duration)
        else:
            duration_of_calls[calling] += int(duration)
        if receiving not in duration_of_calls.keys():
            duration_of_calls[receiving] = int(duration)
        else:
            duration_of_calls[receiving] += int(duration)
longest_call = max(duration_of_calls.values())
longest_call_number = ''
for k in duration_of_calls.keys(): 
    if duration_of_calls[k] == longest_call: 
        longest_call_number = k

print(str(longest_call_number) + " spent the longest time, " + str(longest_call) +" seconds, on the phone during September 2016.")
