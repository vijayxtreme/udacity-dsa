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

phone_numbers = set()

def add_numbers_to_set(phone_numbers, records):
    for record in records:
        phone = record[0]
        phone_numbers.add(phone)
        phone = record[1]
        phone_numbers.add(phone)


add_numbers_to_set(phone_numbers, texts)
add_numbers_to_set(phone_numbers, calls)
print("There are " + str(len(phone_numbers)) + " different telephone numbers in the records.")

# O(N) Time - has to loop through all text and call records, which is O(2N)
# but dropping constants brings this to O(N) Time
# O(1) Space - fixed amount of space for the text and call records