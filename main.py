from functions import *
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


if __name__ == '__main__':
    init()
    main() if (input("1 = main flow\nelse = show graph\n: ")== "1") else show()
