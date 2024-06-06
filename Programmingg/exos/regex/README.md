# Python Regex Exercises

## 1. Create a regex that finds integers without size limit.
``` 
import re

pattern = r"\d+"
s = "sssgdds888sfsfs88"

result = re.findall(pattern, s)
print(result) 
```

## 2. Create a regex that finds negative integers without size limit.
```
import re

pattern = r"-\d+"
s = "sssgdds-888sfsfs88"

result = re.findall(pattern, s)
print(result)
```

## 3. Create a regex that finds (positive or negative) integers without size limit.
```
import re

pattern = r"-?\d+"
s = "sssgdds-888sfsfs88"

result = re.findall(pattern, s)
print(result)
```
## 4. Capture all the numbers of the following sentence :
```

```

