from functions.df_tools import *

def getpatient_info():
    patient_status = input("Is the patient a bed-ridden patient? ")
    return patient_status

def select_vaccine():
    vaccine = int(input("1 = Sinovac\n2 = Sinopharm\n3 = AstraZeneca\n4 = Pfizer\n"))
    if vaccine == 1:
        return "Sinovac"
    elif vaccine == 2:
        return "Sinopharm"
    elif vaccine == 3:
        return "AstraZeneca"
    else:
        return "Pfizer"
        
def select_Hospital():
    hospital = int(input("1 = Hospital1\n2 = Hospital2\n3 = Hospital3\n4 = Hospital4\n"))
    if hospital == 1:
        return "Hospital1"
    elif hospital == 2:
        return "Hospital2"
    elif hospital == 3:
        return "Hospital3"
    else:
        return "Hospital4"

def main(id):
    p_status = getpatient_info()
    if(p_status == "yes"):
        address = input("Your address: ")
        print(f"{id = }")
        updateWithCondition("schedual.txt", "ID card", id, "location", address)
    vaccine = select_vaccine()
    print(vaccine)
    updateWithCondition("schedual.txt", "ID card", id, "Vaccine name", vaccine)
    if(p_status != "yes"):
        hospital = select_Hospital()
        print(hospital)
        updateWithCondition("schedual.txt", "ID card", id, "location", hospital)

if __name__ == '__main__':
    main()