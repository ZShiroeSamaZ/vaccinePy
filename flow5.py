from os import read
from df_tools import *

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


def update_status(type):
    situation, history = readTxt("situation_status.txt").values[-1]
    if(type == "situation"):
        situation += 1
        print("registration situation =", situation)
    else:
        history += 1
        print("vaccination history =", history)
    appendTxt("situation_status.txt", [situation, history], ["registration", "history"])

def registration_situation():
    id_card = int(input("ID card: "))
    df = readTxt("user.txt")
    query_by_id = df_filter(df, "ID card", id_card)
    if(~query_by_id):
        print("You have not registered")
    else:
        printInfo(query_by_id)
        df = readTxt("schedual.txt")
        df = df_filter(df, "ID card", id_card)
        id_card, vac_name, location, date, time = df
        print("Vaccine name: ", vac_name)
        print("Location: ", location)
        print("New date: ", date)
        print("Time: ", time)
    update_status("situation")
    


def vac_history():
    id_card = int(input("ID card: "))
    df = readTxt("user.txt")
    query_by_id = df_filter(df, "ID card", id_card)
    if(~query_by_id):
        print("You have not registered")
    else:
        printInfo(query_by_id)
        df = readTxt("schedual.txt")
        df = df_filter(df, "ID card", id_card)
        id_card, vac_name, location, date, time = df
        print("Vaccine name: ", vac_name)
        print("Location: ", location)
        df = readTxt("vaccine.txt")
        df = df_filter(df, "ID card", id_card)
        id_card, first, second = df
        print("First dose: ", first)
        print("Second dose: ", second)
    update_status("history")

if __name__ == '__main__':
    quantity_vac = input("quantity of vaccine: ")
    service_type = int(input("1 = Check the registration situation\n2 = Check vaccine history\n"))
    if(service_type == 1):
        registration_situation()
    else:
        vac_history()