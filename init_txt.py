from df_tools import *

if __name__ == '__main__':
    initTxt("user.txt", ['name', 'age', 'sex', "phone number",
                         "ID card", "date of birth", "congenital disase"])
    initTxt("schedual.txt", ["ID card",
            "Vaccine name", "location", "date", "time"])
    initTxt("vaccine.txt", ["ID card", "first dose", "second dose"])
    initTxt("vaccine_amount.txt", ["sinovac", "sinopharm", "astra", "pfizer"])
    appendTxt("vaccine_amount.txt", [1000000,1000000,1000000,1000000], ["sinovac", "sinopharm", "astra", "pfizer"])
    initTxt("situation_status.txt", ["registration", "history"])
    appendTxt("situation_status.txt", [0, 0], ["registration", "history"])