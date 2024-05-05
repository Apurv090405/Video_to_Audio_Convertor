import re

# i) compile() - Compiles a regular expression pattern into a regular expression object
pattern = re.compile(r'\d{3}-\d{2}-\d{4}')

# ii) finditer() - Finds all occurrences of a pattern in a string and returns an iterator of match objects
text = "My SSN is 123-45-6789 and another SSN is 987-65-4321"
matches = pattern.finditer(text)
for match in matches:
    print("Found SSN:", match.group())

# iii) match() - Determines if the regular expression matches at the beginning of the string
result = re.match(r'\d{3}', '123-45-6789')
print("Match found at the beginning:", result.group() if result else "No match")

# iv) fullmatch() - Determines if the regular expression matches the entire string
result = re.fullmatch(r'\d{3}-\d{2}-\d{4}', '123-45-6789')
print("Full match:", result.group() if result else "No match")

# v) search() - Searches for the first occurrence of a pattern in a string
result = re.search(r'\d{3}', '123-45-6789')
print("First occurrence found:", result.group() if result else "No match")

# vi) findall() - Finds all occurrences of a pattern in a string and returns them as a list
results = re.findall(r'\d{3}', '123-45-6789 987-65-4321')
print("All occurrences found:", results)

# vii) sub() - Replaces occurrences of a pattern in a string with a replacement string
new_text = re.sub(r'\d{3}', 'XXX', '123-45-6789 987-65-4321')
print("Text after substitution:", new_text)

# viii) subn() - Replaces occurrences of a pattern in a string with a replacement string and returns the new string along with the number of substitutions made
new_text, count = re.subn(r'\d{3}', 'XXX', '123-45-6789 987-65-4321')
print("Text after substitution:", new_text)
print("Number of substitutions made:", count)

# ix) split() - Splits a string into substrings using a regular expression pattern as the delimiter
parts = re.split(r'\s', 'This is a test')
print("Split parts:", parts)
