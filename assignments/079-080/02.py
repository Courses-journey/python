# Today Is "2021, 8, 10"

"2021-08-10"
"Aug 10, 2021"
"10 - Aug - 2021"
"10 / Aug / 21"
"10 / August / 2021"
"Tue, 10 August 2021"
from datetime import datetime


today =datetime.now()
print(today.date())
print(today.strftime("%b %d, %Y"))
print(today.strftime("%d - %b - %Y"))
print(today.strftime("%d / %b / %y"))
print(today.strftime("%d / %B / %Y"))
print(today.strftime("%a,%d %b %Y"))