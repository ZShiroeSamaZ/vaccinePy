from functions.df_tools import *
from datetime import date

def printInfo(info):
    name,age,sex,phone_num,id_card,date_of_birth,disease = info
    print("------------")
    print("Name: ", name)
    print("Age: ", age)
    print("Sex: ", sex)
    print("Phone Number: ", phone_num)
    print("ID card: ", id_card)
    print("Date Of Birth: ", date_of_birth)
    print("Congenital Disease: ", disease)

def datenow():
    day = str(date.today().day)
    month = str(date.today().month)
    year = str(date.today().year)
    date_now = day+"/"+month+"/"+year
    return date_now

def update_status(type):
    data = readTxt("situation_status.txt")
    situation, history, _ = data.sum()
    if(type == "situation"):
        situation += 1
        print("registration situation =", situation)
        appendTxt("situation_status.txt", [1, 0, datenow()], ["registration", "history", "date"])
    else:
        history += 1
        print("vaccination history =", history)
        appendTxt("situation_status.txt", [0, 1, datenow()], ["registration", "history", "date"])

def registration_situation():
    id_card = int(input("ID card: "))
    df = readTxt("user.txt")
    query_by_id = df_filter(df, "ID card", id_card)
    if(query_by_id.empty):
        print("You have not registered")
    else:
        printInfo(query_by_id.values[0])
        df = readTxt("schedual.txt")
        df = df_filter(df, "ID card", id_card)
        id_card, vac_name, location, date, time = df.values[0]
        print("Vaccine name: ", vac_name)
        print("Location: ", location)
        print("New date: ", date)
        print("Time: ", time)
    update_status("situation")
    


def vac_history():
    id_card = (input("ID card: "))
    df = readTxt("user.txt")
    query_by_id = df_filter(df, "ID card", int(id_card))
    if(query_by_id.empty):
        print("You have not registered")
    else:
        printInfo(query_by_id.values[0])
        df = readTxt("schedual.txt")
        df = df_filter(df, "ID card", int(id_card))
        id_card, vac_name, location, date, time = df.values[0]
        print("Vaccine name: ", vac_name)
        print("Location: ", location)

        df = readTxt("vaccine.txt")
        df = df_filter(df, "ID card", id_card)
        id_card, first, second = df.values[0]
        print("First dose: ", first)
        print("Second dose: ", second)

    update_status("history")

def main():
    print_vaccine_amount()
    service_type = int(input("1 = Check the registration situation\n2 = Check vaccine history\n"))
    if(service_type == 1):
        registration_situation()
    else:
        vac_history()

if __name__ == '__main__':
    main()