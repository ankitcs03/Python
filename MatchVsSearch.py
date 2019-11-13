# As the re.match documentation says:
# -----------------------------------------------------------------
# If zero or more characters at the beginning of string match the regular expression pattern, 
# return a corresponding MatchObject instance. Return None if the string does not match the pattern;
#  note that this is different from a zero-length match.

# Note: If you want to locate a match anywhere in string, use search() instead.

# re.search searches the entire string, as the documentation says:
# -----------------------------------------------------------------
# Scan through string looking for a location where the regular expression pattern produces a match,
#  and return a corresponding MatchObject instance. Return None if no position in the string matches 
# the pattern; note that this is different from finding a zero-length match at some point in the string.

import re

string_with_newline = """something 
someotherthing"""

print(re.match('some',string_with_newline))  # match
print(re.match('someother',string_with_newline))  # won't matched
print(re.match('^someother', string_with_newline, re.MULTILINE) )# also won't match
print("---------------------------------------------")
print(re.search('someother',string_with_newline))
print(re.search('^someother',string_with_newline,re.MULTILINE))
print("---------------------------------------------")
m = re.compile('thing$', re.MULTILINE)
print (m.match(string_with_newline) ) # no match
print (m.match(string_with_newline, pos=4)) # matches
print (m.search(string_with_newlinels, re.MULTILINE) )# also matches



Output:

<re.Match object; span=(0, 4), match='some'>
None
None
---------------------------------------------
<re.Match object; span=(11, 20), match='someother'>
<re.Match object; span=(11, 20), match='someother'>
---------------------------------------------
None
None
<re.Match object; span=(20, 25), match='thing'>
