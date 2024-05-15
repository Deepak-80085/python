# To check number of days lived until today from your birthdate

import re
from datetime import date
def check_birthdate():
    data = (input("Enter your birthdate in YYYY-MM-DD format : "))
    if re.match(r'\d{4}-\d{2}-\d{2}',data):
        return data
    else:
        print("Invalid format. Please enter the date in the format YYYY-MM-DD.")
def check(birthdate):
    today = date.today()
    no_of_days = (today - birthdate).days
    years = no_of_days // 365
    no_of_months = (no_of_days ) // 30 
    months = (no_of_days - (years * 365)) // 30
    days = (no_of_days - (years * 365) -(months * 30))
    print("no of days are :",no_of_days)
    print("no of months",no_of_months)
    print("no of year : ",years)
    print(f"Therefore total no years {years}, months {months}, days {days}")

def main():
    birthdate = check_birthdate()
    check(date.fromisoformat(birthdate))

main()                                                                                                  

