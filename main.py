import re
from textwrap import wrap


old_string = 'This is a query where I select*stuff and other selections from a database.'
print('ORIGINAL:')
print(old_string, '\n')

# if 'select' in old_string:
#     query2 = old_string.replace('select', 'SELECT')
#     print(query2)


# \b is the word boundary metacharcater. Use this when you want to search for an EXACT word, not just a substring
# syntax for re.sub is re.sub('old word', 'new word', 'string')

replace_substring = re.sub('select', 'SELECT', old_string)
print('REPLACE SUBSTRING:')
print(replace_substring, '\n')

replace_exact = re.sub(r'\bselect\b', 'SELECT', old_string)
print('REPLACE EXACT STRING:')
print(replace_exact, '\n')

replace_exact_newline = re.sub(r'\bselect\b', '\nSELECT', old_string)
replace_exact_newline2 = re.sub(r'\bfrom\b', '\nFROM', replace_exact_newline)
print('REPLACE EXACT STRING + NEW LINE:')
print(replace_exact_newline2, '\n')

# Find number of full words in the string
num_words = len(re.findall(r'\w+', old_string))
print('There are', num_words, 'words in the original string.')

# Start new line after certain number of words
