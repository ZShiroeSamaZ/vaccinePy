from df_tools import *

def getServiceType():
    input_value = int(input("1 = register\n2 = reschedule\n: "))
    return input_value

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
    if(~query_by_id):
        print("You are not registered")
        return False
    else:
        printInfo(query_by_id)
        new_date = input("New Date: ")
        return new_date, id_card

if __name__ == '__main__':
    user_template = ['name', 'age', 'sex', "phone number",
                "ID card", "date of birth", "congenital disase"]
    schedual_template = ["ID card",
            "Vaccine name", "location", "date", "time"]
    vaccine_template =  ["ID card", "first dose", "second dose"]

    if(getServiceType() == 1):
        df_input, id_card = register()
        appendTxt("user.txt", df_input, user_template)
        appendTxt("schedual.txt", [id_card, "", "", "", ""], schedual_template)
        appendTxt("vaccine.txt", [id_card, "", ""], vaccine_template)

    else:
        info_data = reschedule()
        if(~info_data):
            pass
        else:
            new_date, id_card = info_data
            schedual_df = readTxt("schedual.txt")
            df = updateWithCondition("schedual.txt", "ID card", id_card, "date", new_date)
            writeTxt("schedual.txt", df)
            print("\n", df.iloc[-1])
    