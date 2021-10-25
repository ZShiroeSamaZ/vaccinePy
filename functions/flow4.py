from functions.df_tools import *

def select_vaccine(vaccine_amount):
    vaccine = int(input("1 = Sinovac\n2 = Sinopharm\n3 = AstraZeneca\n4 = Pfizer\n"))
    vaccine_index = vaccine - 1
    vaccine_amount[vaccine_index] -= 2
    if vaccine == 1:
        return "Sinovac", vaccine_index
    elif vaccine == 2:
        return "Sinopharm", vaccine_index
    elif vaccine == 3:
        return "AstraZeneca", vaccine_index
    else:
        return "Pfizer", vaccine_index

def main(id):
    vaccine_amount = readTxt("vaccine_amount.txt").values[-1]
    print_vaccine_amount()
    vaccine, index = select_vaccine(vaccine_amount)
    print(vaccine)
    updateWithCondition("vaccine.txt", "ID card", int(id), "first dose", vaccine)
    updateWithCondition("vaccine.txt", "ID card", int(id), "second dose", vaccine)
    print(vaccine, "amont: ", vaccine_amount[index], "\n")
    df = appendTxt("vaccine_amount.txt", vaccine_amount, ["sinovac", "sinopharm", "astra", "pfizer"])
    print(df.iloc[-1])

if __name__ == '__main__':
    main()