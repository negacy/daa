"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import sys
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.
Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
#part A
def getAreaCodesCalledByPplFromBanglore(calls):
    area_codes_called_by_ppl_in_banglore = []
    for line in calls:
        caller = line[0].strip()
        if caller.startswith('(080)'):#calls originating from Banglore
            receiver = line[1].strip() 
            #land line receivers
            if receiver.startswith('(0') and ')' in receiver:
                area_code = receiver.split(')')[0] + ')'
                area_codes_called_by_ppl_in_banglore.append(area_code)
            #mobile receivers
            elif ' ' in receiver:
                mobile_pref = receiver[:4]
                if mobile_pref.startswith('7') or mobile_pref.startswith('8') or mobile_pref.startswith('9'):
                    area_codes_called_by_ppl_in_banglore.append(mobile_pref)
            #Telemarketers
            elif receiver.startswith('140'):
                area_codes_called_by_ppl_in_banglore.append('140')
    return set(area_codes_called_by_ppl_in_banglore )
#part B
def getfixed2fixedRaitioInBanglore(calls):
    cnt_banglore_fixed_line_caller = 0
    cnt_banglore_fixed_line_receiver = 0
    for line in calls:
        caller = line[0].strip()
        receiver = line[1].strip()
        if caller.startswith('(0') and caller[:5] == '(080)':
            cnt_banglore_fixed_line_caller += 1
            if receiver.startswith('(0') and receiver[:5] == '(080)':
                cnt_banglore_fixed_line_receiver += 1
    percent = cnt_banglore_fixed_line_receiver/cnt_banglore_fixed_line_caller*100
    return percent

#sort in lexicographic order
print("The numbers called by people in Bangalore have codes:")
for area_code in sorted(getAreaCodesCalledByPplFromBanglore(calls)):
    print(area_code)
print("%.2f percent of calls from fixed lines in Bangalore are calls" % getfixed2fixedRaitioInBanglore(calls))
