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

## Date and Time ([docs](https://docs.python.org/3/library/datetime.html#module-datetime))

```
import datetime
```

### Dates

Represents a date in the ideal Gregorian calendar.

Initialization:
```
date(year, month, day)
```

Get today's date:
```
date.today()
```

Get the date of a timestamp object:
```
date.fromtimestamp([timestamp])
```

Get the date from an ISO 8601 format string:
```
date.fromisoformat([string])
```

Get a date with modified parameters:
```
date.replace([year], [month], [self])
```

### Time

The local time of day, independent of any particular day.

Initialize:
```
datetime.time([hour], [minute], [second], [microsecond], [timezone], ...)
```

Get time from an ISO format string:
```
time.fromisoformat([string])
```

Replace some components of the time:
```
time.replace([hour], [minute], [second], [microsecond], [timezone], ...)
```

Get an ISO format string for the time:
```
time.isoformat(...)
```

### Datetimes

An object containing all information from a Date and a Time.

Initialize:
```
datetime([year], [month], [day], [hour], [minute], [second], [microsecond], [timezone], ...)
```

Get the current time as a `datetime`, with no time zone information:
```
datetime.today()
```

Get the current time as a `datetime`, optionally passing time zone information:
```
datetime.now([timezone])
```

Get the current UTC time as a `datetime`
```
datetime.utcnow()
```

Get `datetime` from an ISO 8601 format string:
```
datetime.fromisoformat()
```

Get a POSIX timestamp from the `datetime`
```
datetime.timestamp()
```
- Same format as time.time()

Get an ISO format timestamp string for the `datetime`:
```
datetime.isoformat
```

### Time Zones

Can be represented with the class `datetime.timezone`

Initialization:
```
datetime.timezone([offset])
```
- Offset is a `timedelta` object with a value between -24 hours and +24 hours.

Get the time zone's offset from UTC as a `timedelta`:
```
timezone.utcoffset()
```

## timedelta

Represents a delta between two points in time.
- Supports various arithmetical operations

Initialize:
```timedelta(days, seconds, microseconds, milliseconds, minutes, hours, weeks)```

Get the duration in seconds:
```
timedelta.total_seconds()
```
