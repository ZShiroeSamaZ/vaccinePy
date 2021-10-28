import matplotlib.pyplot as plt
from functions.df_tools import *
import pandas as pd

def show_graph(seleted_graph):
    if seleted_graph == 1:
        f = readTxt('user.txt')
        print("Amount of people of Registrants in the same age.")
        data = f.groupby(['age']).size().reset_index(name='counts')
        df = pd.DataFrame(data ,columns=['age','counts'])
        df.plot(x ='age', y='counts', kind = 'bar')
        plt.show()
    elif seleted_graph == 2: 
        f = readTxt('user.txt')
        print("Amount of people of Reschedule in the same day.")
        data = f.groupby(['age']).size().reset_index(name='counts')
        df = pd.DataFrame(data ,columns=['age','counts'])
        df.plot(x ='age', y='counts', kind = 'bar')
        plt.show()


def main():
    print("Show graph")
    seleted_graph = int(input("Select graph 1-10\n: "))
    show_graph(seleted_graph)
    # print(graph)

if __name__ == '__main__':
    main()
    