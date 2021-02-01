from datetime import date
import time

year = 365
hoursWorked = int(input("how many Hours did you work? "))
dayOfYear = date.today().timetuple().tm_yday
remainingDays = year - dayOfYear
print(f"Remaining Days: {remainingDays}")
average = 8
# totalNeeded = (year * average) - hoursWorked
totalNeeded = 3000 - hoursWorked
hourstoWork = totalNeeded / remainingDays

print(f"you need to work {round(hourstoWork,2)} Hours per day")

time.sleep(5)
