
from functions.df_tools import *


def getServiceType():
    input_value = int(input("1 = register\n2 = reschedule\n: "))
    return input_value


def printInfo(info):
    name, age, sex, phone_num, id_card, date_of_birth, disease = info
    print("------------")
    print("Name: ", name)
    print("Age: ", age)
    print("Sex: ", sex)
    print("Phone Number: ", phone_num)
    print("ID card: ", id_card)
    print("Date Of Birth: ", date_of_birth)
    print("Congenital Disease: ", disease)


def register():
    name = input("Name: ")
    age = input("Age: ")
    sex = input("Sex: ")
    phone_num = input("Phone Number: ")
    id_card = input("ID card: ")
    date_of_birth = input("Date Of Birth: ")
    disease = input("Congenital Disease: ")
    df_input = [name, age, sex, phone_num, id_card, date_of_birth, disease]
    printInfo(df_input)
    return df_input, id_card


def reschedule():
    id_card = int(input("ID Card: "))
    df = readTxt("user.txt")
    query_by_id = df_filter(df, "ID card", id_card)
    if(query_by_id is False):
        print("You are not registered")
        return False
    else:
        printInfo(query_by_id.values[-1])
        new_date = input("New Date: ")
        return new_date, id_card

def is_ID_Exist(id):
    user_df = readTxt("user.txt")
    founded = df_filter(user_df, "ID card", id)
    if(founded is not False):
        return True
    else:
        return False

def main():
    if(getServiceType() == 1):
        user_template = ['name', 'age', 'sex', "phone number",
                         "ID card", "date of birth", "congenital disase"]
        schedual_template = ["ID card",
                            "Vaccine name", "location", "date", "time"]
        vaccine_template = ["ID card", "first dose", "second dose"]
        
        df_input, id_card = register()
        print(is_ID_Exist(id_card))
        if(is_ID_Exist(id_card) is True):
            print("User with ID:", id_card, "Exist")
            exit()
        else:
            appendTxt("user.txt", df_input, user_template)
            appendTxt("schedual.txt", [id_card, "-",
                                    "-", "-", "-"], schedual_template)
            appendTxt("vaccine.txt", [id_card, "-", "-"], vaccine_template)

    else:
        info_data = reschedule()
        if(info_data is False):
            pass
        else:
            new_date, id_card = info_data
            df = readTxt("user.txt")
            df = df_filter(df, "ID card", id_card)
            printInfo(df.values[-1])
            df = updateWithCondition(
                "schedual.txt", "ID card", id_card, "date", new_date)
            df = df_filter(df, "ID card", id_card)
            df = df.drop(columns="ID card")
            print(df.iloc[-1])
    return int(id_card)


if __name__ == '__main__':
    main()
