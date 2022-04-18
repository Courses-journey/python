import datetime

today = datetime.datetime.now()
needed = datetime.datetime(2021,6,25)
# The Date Is "2021, 6, 25"
# Today Is "2021, 8, 10"

# Message Will Be
"Days From 2021-06-25 To 2021-08-10 Is => 46"

print(f"Days From {needed.date()} To {today.date()} Is => {(today-needed).days}")