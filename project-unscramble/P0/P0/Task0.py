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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

first_record = texts[0]
last_record = calls[-1]
print("First record of texts " + first_record[0] + " texts " + first_record[1] + " at time " + first_record[2])
print("Last record of calls " + last_record[0] + " calls " + last_record[1] + " at time " + last_record[2] + ", lasting " + last_record[3] + " seconds")

# O(1) Time - retrieving the first and last records are constant time operations
# O(1) Space - the space for the call list is constant.