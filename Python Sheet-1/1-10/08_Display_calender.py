# 8. Write a Python program to display calendar?

import calendar

ch = calendar.weekday(2024, 8, 1)
print(ch)

if ch == 0:
    print("Monday")
elif ch == 1:
    print("Tuesday")
elif ch == 2:
    print("Wednesday")
elif ch == 3:
    print("Thursday")
elif ch == 4:
    print("Friday")
elif ch == 5:
    print("Saturday")
elif ch == 6:
    print("Sunday")