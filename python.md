# Python

## File I/O ([docs](https://docs.python.org/3/tutorial/inputoutput.html))

### Read text from a file

Open file:
```
with open([filename], "r") as file_data:
```

Read all text from file:
```
file_data.read()
```

Read next line from file:
```
file_data.readline()
```

### Write text to a file

Open file:
```
with open([filename], [mode]) as file_data:
```
- Use mode `"w"` to replace any existing file contents
- Use mode `"w+` to append to the file

Write text to document:
```
file_data.write([text])
```

## JSON ([docs](https://docs.python.org/3/library/json.html#module-json))

```
import json
```

Serialize structured data to JSON:
```
json.dumps([data])
```

Read JSON from a string:
```
json.loads([string])
```

## Random ([docs](https://docs.python.org/3/library/random.html#random.randint))

```
import random
```

Random float between 0 and 1:
```
random.random()
```

Random integer:
```
random.randint([min], [max])
```
- min and max are inclusive

Choose element from array:
```
random.choice([array])
```
