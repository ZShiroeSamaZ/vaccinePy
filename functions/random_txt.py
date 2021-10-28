from functions.df_tools import *
import names
import random
import os
from datetime import date

def ran_range(min, max):
    ran = random.randint(min, max)
    return ran

def user(number):
    user_template = ['name', 'age', 'sex', "phone number",
                         "ID card", "date of birth", "congenital disase"]
    for id in range(number):    
        gender = "male" if ran_range(0, 10)<=5 else "female"
        name = names.get_full_name(gender=gender)
        age = ran_range(10, 60)
        phone = ""
        ph_no = ["0", "8"]
        for i in range(1, 8):
            ph_no.append(str(ran_range(0, 9)))
        phone = phone.join(ph_no)
        day = str(ran_range(1, 30))
        month = str(ran_range(1, 12))
        year = str(date.today().year - age)
        date_of_birth = day+"/"+month+"/"+year
        disease = "None"

        to_write = [name, age, gender, phone, id, date_of_birth, disease]
        appendTxt("user.txt", to_write, user_template)


def schedual(number):
    schedual_template = ["ID card",
                            "Vaccine name", "location", "date", "time"]
    for id in range(number):    
        vaccine = ["Sinovac", "Sinopharm", "AstraZeneca", "Pfizer"]
        hospital = ["Hospital1", "Hospital2", "Hospital3", "Hospital4"]
        selected_vac = vaccine[ran_range(0, 3)]
        selected_hos = hospital[ran_range(0, 3)]
        day = str(ran_range(1, 30))
        month = str(ran_range(1, 12))
        year = str(date.today().year + ran_range(0, 1))
        date_schedual = day+"/"+month+"/"+year
        time = str(ran_range(10, 16)) + ":" + str(ran_range(10, 59))

        to_write = [id, selected_vac, selected_hos, date_schedual, time]
        appendTxt("schedual.txt", to_write, schedual_template)


def vaccine(number):
    vaccine_template = ["ID card", "first dose", "second dose"]
    for id in range(number):    
        vaccine = ["Sinovac", "Sinopharm", "AstraZeneca", "Pfizer"]
        selected_vac = vaccine[ran_range(0, 3)]
        to_write = [id, selected_vac, selected_vac]
        appendTxt("vaccine.txt", to_write, vaccine_template)




def main(num):
    user(num)
    schedual(num)
    vaccine(num)


if __name__ == '__main__':
    main(10)
