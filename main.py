from functions import *


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
    main() if (input("1 = main flow\nelse = show graph\n: ")== "1") else show()
