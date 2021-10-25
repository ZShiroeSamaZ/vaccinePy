import pandas as pd

def initTxt(filename, template):
    df = pd.DataFrame(columns=template)
    df.to_csv("./data/" + filename, index=None, sep=",")

def readTxt(filename):
    df = pd.read_csv("./data/" + filename, sep=",")
    return df

def writeTxt(filename, data_frame):
    df = pd.read_csv("./data/" + filename, sep=",")
    df = data_frame
    df.to_csv("./data/" + filename, index=None, sep=",")
    return df
    
def appendTxt(filename, data, template):
    df = pd.read_csv("./data/" + filename, sep=",")
    input_data = pd.DataFrame([data], columns=template)
    df = df.append(input_data, ignore_index=True)
    df.to_csv("./data/" + filename, index=None, sep=",")
    return df

def updateWithCondition(filename, key_column, condition_value, update_column, update_value):
    df = readTxt(filename)
    df.loc[(df[key_column] == condition_value), update_column] = update_value
    writeTxt(filename, df)
    return df

def df_filter(df, key_column, condition_value):
    query = False
    try:
        query = df.loc[(df[key_column] == condition_value)]
        query.drop(columns="ID card")
        query.values[0]
    except IndexError:
        pass
        # print("You have not registered")
        # exit()
        # raise FileNotFoundError("Not found user with selected ID")
    return query

def print_vaccine_amount():
    vaccine_amount = readTxt("vaccine_amount.txt").values[-1]
    print("Sinovac", vaccine_amount[0])
    print("Sinopharm", vaccine_amount[1])
    print("AstraZeneca", vaccine_amount[2])
    print("Pfizer", vaccine_amount[3])