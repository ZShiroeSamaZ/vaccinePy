from functions import *
from functions import random_txt
from functions.df_tools import *

def init():
    try:
        readTxt("user.txt")
    except:
        init_txt.main()

def main():
    print('********1**********')
    id_card = f1.main()
    print('********2**********')
    f2.main(id_card)
    print('********3**********')
    f3.main(id_card)
    print('********4**********')
    f4.main(id_card)
    print('********5**********')
    f5.main()


def show():
    graph.main()

def overWrite():
    user_num = int(input("How many user you want to random? : "))
    init_txt.main()
    random_txt.main(user_num)

if __name__ == '__main__':
    init()
    selected = int(input("1 = main flow\n2 = show graph\n99 = overWrite\n: "))
    if(selected == 1): main()
    elif(selected == 2): show()
    elif(selected == 99): overWrite()
    
