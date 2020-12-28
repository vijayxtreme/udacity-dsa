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

'''
Psuedocode
longest time on the phone revise
caller who spent longest time on phone is the __total time they made and received calls__ 
make a dict with longest caller that has longest time, and phone id.  Set to zero
loop thru all calls 
 add caller in col0 to dict with time spent on phone
 if caller already exists, update time spent on phone
 if time is bigger than longest time, then update longest caller

loop thru all calls
 add caller in col1 to dict with time spent on phone
 if caller already exists, update time spent on phone
 if time is bigger than longest time, then update longest caller

Should run O(N) time.
'''

callers = {}
longest_caller = (None, 0)

# Explore col1 cols (outgoing calls)
for call in calls:
    time = int(call[3]) # get the time for this call row

    for i in range(0,2):
        caller = call[i]
        if caller in callers:
            callers[caller] += time
            if longest_caller[1] < callers[caller]:
                longest_caller = (caller, callers[caller])
        else: 
            callers[caller] = 0

print(longest_caller[0] + " spent the longest time, " + str(longest_caller[1]) + " seconds, on the phone during September 2016.")

# O(N) Time - even though we iterate through a fixed range 2 columns to get the 
# outgoing caller and the incoming caller per loop, it's a constant iteration
# so this is just O(N*2) which after dropping the constant becomes O(N)
# O(1) Space - for just a few variables and the call list
