def zeller_congruence(day, month, year):
    #Zeller's congruence; algorithm devised by Christian Zeller in the 19th century
    #used to calculate the day of the week for any Julian or Gregorian calendar date.
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    h = (day + ((13 * (month + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j)) % 7
    days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days_of_week[h]

day = 15
month = 4
year = 2024

day_of_week = zeller_congruence(day, month, year)
print(f"The {day}th of {month}/{year} falls on a {day_of_week}.")
