# Prompt the user to enter a date in the form mm/dd/yyyy
date = input("Enter a date in the form mm/dd/yyyy: ")

# Split the date into its components
month, day, year = date[0:2], date[3:5], date[6:]

# Decleare a final date string
final_date = ""

# Check the month
if month == "01":
    final_date += "January"
elif month == "02":
    final_date += "February"
elif month == "03":
    final_date += "March"
elif month == "04":
    final_date += "April"
elif month == "05":
    final_date += "May"
elif month == "06":
    final_date += "June"
elif month == "07":
    final_date += "July"
elif month == "08":
    final_date += "August"
elif month == "09":
    final_date += "September"
elif month == "10":
    final_date += "October"
elif month == "11":
    final_date += "November"
elif month == "12":
    final_date += "December"

# Add the day and year to the final date
final_date += " " + day + ", " + year

# Print the final date
print(final_date)
