import re

pattern = r"\d+"
text = "21 scouts and 3 tanks fought against 4,003 protestors, so the manager was not 100.00% happy."

result = re.findall(pattern, text)
print(result)
