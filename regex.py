import re

# Example to Find and Trim User Number
# text = "+92-3107860423"
# pattern = r"\d+"
# matchNum = re.findall(pattern,text)
# actualNum = "0"+matchNum[1]
# print(actualNum)

# Example to find Specific substring
# text = "I love Pakistan. pakistan is a lovely country "
# pattern = r"[A-Z a-z]akistan"
# print(re.findall(pattern,text))

expression = "abbc"
pattern = r"^a*|c$"
print(re.findall(pattern,expression))
