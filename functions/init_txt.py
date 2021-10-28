from functions.df_tools import *
import os
from datetime import date

def datenow():
    day = str(date.today().day)
    month = str(date.today().month)
    year = str(date.today().year)
    date_now = day+"/"+month+"/"+year
    return date_now
    
def main():
    try:
        os.mkdir("./data")
    except:
        pass
    
    initTxt("user.txt", ['name', 'age', 'sex', "phone number",
                         "ID card", "date of birth", "congenital disase"])
    initTxt("schedual.txt", ["ID card",
            "Vaccine name", "location", "date", "time"])
    initTxt("vaccine.txt", ["ID card", "first dose", "second dose"])
    initTxt("vaccine_amount.txt", ["sinovac", "sinopharm", "astra", "pfizer"])
    appendTxt("vaccine_amount.txt", [1000000, 1000000, 1000000, 1000000], [
              "sinovac", "sinopharm", "astra", "pfizer"])
    initTxt("situation_status.txt", ["registration", "history"])


if __name__ == '__main__':
    main()
