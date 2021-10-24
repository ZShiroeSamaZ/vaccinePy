
from df_tools import appendTxt, readTxt, writeTxt


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

if __name__ == '__main__':
    vaccine_amount = readTxt("vaccine_amount.txt").values[-1]
    vaccine, index = select_vaccine(vaccine_amount)
    print(vaccine)
    print(vaccine, "amont: ", vaccine_amount[index], "\n")
    df = appendTxt("vaccine_amount.txt", vaccine_amount, ["sinovac", "sinopharm", "astra", "pfizer"])
    print(df.iloc[-1])