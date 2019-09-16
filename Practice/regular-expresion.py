import re

# ################# Search
test = 'I am Rakib'
# result = re.search(r'R\w\w\w\w', test)
# print(result.group())

# ################# Findall
# result = re.findall(r'a\w', test)
# print(result)

# ################@# Match
# result = re.match(r'R\w\w\w', test)
# print(result)

# ################@# Split
# result = re.split(r"\s+",test)
# print(result)

# ################@# Substring
result = re.sub(r'\s+','-', test)
print(result)