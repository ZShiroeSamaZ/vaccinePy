import pandas as pd

def initTxt(filename, template): # init dataframe
    df = pd.DataFrame(columns=template)
    df.to_csv("./data/" + filename, index=None, sep=",")

def readTxt(filename): # read dataframe
    df = pd.read_csv("./data/" + filename, sep=",")
    return df

def writeTxt(filename, data_frame): # overwrite dataframe
    df = pd.read_csv("./data/" + filename, sep=",")
    df = data_frame
    df.to_csv("./data/" + filename, index=None, sep=",")
    return df
    
def appendTxt(filename, data, template): # append to dataframe
    df = pd.read_csv("./data/" + filename, sep=",")
    input_data = pd.DataFrame([data], columns=template)
    df = df.append(input_data, ignore_index=True)
    df.to_csv("./data/" + filename, index=None, sep=",")
    return df

def updateWithCondition(filename, key_column, condition_value, update_column, update_value): # update dataframe accordding to key_column
    df = readTxt(filename)
    df.loc[(df[key_column] == condition_value), update_column] = update_value
    writeTxt(filename, df)
    return df

def df_filter(df, key_column, condition_value): # get dataframe row based on condition
    query = False
    try:
        query = df.loc[(df[key_column] == condition_value)]
        query.drop(columns="ID card")
        query.values[0]
    except:
        pass
    return query

def print_vaccine_amount(): # print current vaccine amount
    vaccine_amount = readTxt("vaccine_amount.txt").values[-1]
    print("Sinovac", vaccine_amount[0])
    print("Sinopharm", vaccine_amount[1])
    print("AstraZeneca", vaccine_amount[2])
    print("Pfizer", vaccine_amount[3])