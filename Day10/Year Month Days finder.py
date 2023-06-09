def is_leap(year):
  global leap
  if year % 4 == 0:
    if year % 100 == 0 and year % 400 == 0:
      leap = "True"
      return True
    if year % 100 == 0 and year % 400 != 0:
      leap = "False"
      return False
    if year % 100 != 0 and year % 400 != 0:
      leap = "True"
      return True
  elif year % 4 != 0:
    leap = "False"
    return False
  

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  is_leap(year)
  if leap == "True":
    month_days[1] = 29
  else:
    pass
  return month_days[month-1]

print("Welcome to the year month days finder:\n")
while True:
  year = int(input("Enter a year: "))
  month = int(input("Enter a month: "))
  days = days_in_month(year, month)
  print(days)