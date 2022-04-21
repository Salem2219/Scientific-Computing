# Scientific-Computing
Scientific Computing projects with python

## Arithmetc Formatter

Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:
```
  235
+  52
-----
```

This function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function optionally take a second argument. When the second argument is set to `True`, the answers should be displayed.

### For example

Function Call:
```py
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

Output:
```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

Function Call:
```py
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```

Output:
```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```


## Time Calculator

A function named add_time that takes in two required parameters and one optional parameter:

A start time in the 12-hour clock format (ending in AM or PM)
A duration time that indicates the number of hours and minutes
(optional) A starting day of the week, case insensitive
The function add the duration time to the start time and return the result.

If the result is the next day, it shows (next day) after the time. If the result is more than one day later, it shows (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output displays the day of the week of the result. The day of the week in the output appears after the time and before the number of days later.

Below are some examples of different cases the function handles.

'''
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
'''
