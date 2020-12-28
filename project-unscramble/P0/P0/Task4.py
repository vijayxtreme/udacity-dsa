"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from enum import unique

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

# Revised with effective solution idea, first time heard
# about difference function in Python - thank you.

outgoing = set()
non_telemarketers = set()

# add calls for outgoing to the outgoing set from col[0]
# add calls from col[1] in the non_telemarketers set 
# can't be a telemarketer if number appears in this col
for call in calls:
    outgoing.add(call[0]) # get outgoing caller / texter
    non_telemarketers.add(call[1]) # can't be a telemarketer if in this row
  
# add cols for texts (outgoing/receiving) to the non_telemarketers 
# can't be a telemarketer if sent / received a text, so add to
# non_telemarketers set
for text in texts:
    non_telemarketers.add(text[0])
    non_telemarketers.add(text[1])

# using the difference of sets, get the difference of outgoing and non_telemarketers
# to find telemarketers - since these are just for loops, they are 
# individual O(N) operations or 2 for loops O(2N) - simplified to O(N) operation
telemarketers = outgoing.difference(non_telemarketers)

print("These numbers could be telemarketers: ")
for telemarketer in sorted(telemarketers):
    print(telemarketer)

# Runs O(N log N) Time - searching for telemarketers is just looping through
# N records for calls, adding them to a set of outgoing calls or non_telemarketers
# then going through another loop with N records for texts, and adding
# cols to the non_telemarketers set.
# Two for loops is O(2N), which is simply O(N).  
# Calculating the difference between outgoing and non_telemarketers to get
# telemarketers is a O(1) operation.
# Sorting takes O(N log N) worst case, so this is the bigger
# time operation making this operation O(N log N).

# O(N) space - just need space for the dictionary and set that
# hold the unique callers and telemarketers