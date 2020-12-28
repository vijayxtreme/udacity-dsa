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

import re


def get_area_codes_prefixes(number):
  # is fixed line
  if number[:5] == "(080)":
    return "(080)"
  
  # is a mobile number
  if number[:1] == "9" or number[:1] == "8" or number[:1] == "7":
    return number[:4]

  # is a telemarketer
  if number[:3] == "140":
    return "140"

  # is some other number
  return re.match("\(.+\)", number).group(0)

def get_calls_from_bangalore(calls):
  called_by_bangalore_dict = {"total_calls": 0}

  for call in calls:
    # Someone in Bangalore with fixed line (080) made a call.
    if get_area_codes_prefixes(call[0]) == "(080)":
      # update total calls, we can use it later
      called_by_bangalore_dict["total_calls"] += 1

      # Get the area of code for the receiving caller
      area_code = get_area_codes_prefixes(call[1])
      
      # if this area code exists, update its call count
      if area_code in called_by_bangalore_dict:
        called_by_bangalore_dict[area_code] += 1
      
      # else create a new key with a starting call count of 1
      else:
        called_by_bangalore_dict[area_code] = 1

      

  return called_by_bangalore_dict

def percent_of_bangalore_calls_to_other_calls(calls_by_bangalore):
  # get the calls made to Bangalore 
  # divide by the total calls made by Bangalore
  return round((calls_by_bangalore["(080)"] / calls_by_bangalore["total_calls"] * 100), 2)

# PART A
calls_by_bangalore = get_calls_from_bangalore(calls)
print("The numbers called by people in Bangalore have codes:")
for key in sorted(calls_by_bangalore):
  if key != 'total_calls':
    print(key)


# O(N log N) Time complexity - has to iterate through all calls and 
# do constant time checks on whether call is from Bangalore
# then add to calls_by_bangalore dict.  Printing in lexigraphical order
# using sorted is an O(N log N) operation worst case

# O(N) Space - space for the dict and adding each unique area code

# PART B
percent_of_bangalore = percent_of_bangalore_calls_to_other_calls(calls_by_bangalore)
print(str(percent_of_bangalore) + "% percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

# O(1) Constant Time - getting the percent is just running 
# our percent_of_bangalore_calls_to_other calls function
# which looks up calls_by_bangalore["(080)"] (total calls made to bangalore)
# and divides it by total calls in calls_by_bangalore["total_calls"]

# O(1) Space - No extra space needed to perform this calculation

