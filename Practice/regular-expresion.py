import re

# ################# Search
test = 'I am Rakib and i am a web developer'
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
# result = re.sub(r'\s+','-', test)
# print(result)

# ################# Quantifier
# ### + => Everything afterward
# result = re.findall(r'a\w+', test)
# print(result)
# ### * => 0 or more
# result = re.findall(r'a\w*', test)
# print(result)
# ### ? => 1 character after the first occurrence
# result = re.findall(r'a\w?', test)
# print(result)
# ### {} => Specify
# result = re.findall(r'a\w{1}', test)
# print(result)
# ### {m,n} => Range
# result = re.findall(r'a\w{1,2}', test)
# print(result)