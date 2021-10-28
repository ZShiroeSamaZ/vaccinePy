from collections import defaultdict
import matplotlib.pyplot as plt
from functions.df_tools import *
import pandas as pd
import numpy as np

def filter_df(df, key_column, key_value):
    df = df.loc[(df[key_column] == key_value)]
    return df

def show_graph(seleted_graph):
    if seleted_graph == 6:
        f = readTxt('schedual.txt')
        print("Location with Amount of people of Registrants.")
        data = f.groupby(['location']).size().reset_index(name='counts')
        df = pd.DataFrame(data ,columns=['location','counts'])
        df.plot(x ='location', y='counts', kind = 'bar')
        plt.show()
    elif seleted_graph == 7: 
        f = readTxt('schedual.txt')
        print("Amount of vaccine of Registrants on the same day.")
        data = f.filter(items=['Vaccine name', 'date']).groupby(['date', 'Vaccine name']).size().reset_index(name='counts')
        data.pivot(index='date', columns='Vaccine name', values='counts').plot(kind='bar')
        plt.show()
    elif seleted_graph == 8: 
        f = readTxt("vaccine_amount.txt")
        print("Remaining of vaccine.")
        values = f.values[-1]
        fig, ax = plt.subplots()
        data = {"Sinovac": [values[0]], "Sinopharm": [values[1]], "AstraZeneca": [values[2]], "Pfizer": [values[3]]}
        bar_plot(ax, data, group_stretch=0.8, bar_stretch=0.95, legend=True,
                x_labels=True, label_fontsize=8, barlabel_offset=0.05,
                bar_labeler=lambda k, i, s: str(round(s, 3)))
        fig.show()
        plt.show() 
    elif seleted_graph == 9:
        f = readTxt("situation_status.txt")
        print("Number of round of check the registration situation on the same day.")
        registration = f.filter(items=['registration', 'date']).groupby(['date']).aggregate("sum")
        df = pd.DataFrame(registration ,columns=['registration'])
        df = df.drop(df[df.registration < 1].index)
        df.plot(y='registration', kind = 'bar', use_index = True)
        plt.show() 
    elif seleted_graph == 10:
        f = readTxt("situation_status.txt")
        print("Number of round of Check vaccination historyon the same day.")
        history = f.filter(items=['history', 'date']).groupby(['date']).aggregate("sum")
        df = pd.DataFrame(history ,columns=['history'])
        df = df.drop(df[df.history < 1].index)
        df.plot(y='history', kind = 'bar', use_index = True)
        plt.show() 

def main():
    print("Show graph")
    seleted_graph = int(input("Select graph 1-10\n: "))
    show_graph(seleted_graph)
    # print(graph)

if __name__ == '__main__':
    main()
    


def bar_plot(ax, data, group_stretch=0.8, bar_stretch=0.95,
             legend=True, x_labels=True, label_fontsize=8,
             colors=None, barlabel_offset=1,
             bar_labeler=lambda k, i, s: str(round(s, 3))):
    """
    Draws a bar plot with multiple bars per data point.
    :param dict data: The data we want to plot, wher keys are the names of each
      bar group, and items is a list of bar values for the corresponding group.
    :param float group_stretch: 1 means groups occupy the most (largest groups
      touch side to side if they have equal number of bars).
    :param float bar_stretch: If 1, bars within a group will touch side to side.
    :param bool x_labels: If true, x-axis will contain labels with the group
      names given at data, centered at the bar group.
    :param int label_fontsize: Font size for the label on top of each bar.
    :param float barlabel_offset: Distance, in y-values, between the top of the
      bar and its label.
    :param function bar_labeler: If not None, must be a functor with signature
      ``f(group_name, i, scalar)->str``, where each scalar is the entry found at
      data[group_name][i]. When given, returns a label to put on the top of each
      bar. Otherwise no labels on top of bars.
    """
    sorted_data = list(sorted(data.items(), key=lambda elt: elt[0]))
    sorted_k, sorted_v  = zip(*sorted_data)
    max_n_bars = max(len(v) for v in data.values())
    group_centers = np.cumsum([max_n_bars
                               for _ in sorted_data]) - (max_n_bars / 2)
    bar_offset = (1 - bar_stretch) / 2
    bars = defaultdict(list)
    #
    if colors is None:
        colors = {g_name: [f"C{i}" for _ in values]
                  for i, (g_name, values) in enumerate(data.items())}
    #
    for g_i, ((g_name, vals), g_center) in enumerate(zip(sorted_data,
                                                         group_centers)):
        n_bars = len(vals)
        group_beg = g_center - (n_bars / 2) + (bar_stretch / 2)
        for val_i, val in enumerate(vals):
            bar = ax.bar(group_beg + val_i + bar_offset,
                         height=val, width=bar_stretch,
                         color=colors[g_name][val_i])[0]
            bars[g_name].append(bar)
            if  bar_labeler is not None:
                x_pos = bar.get_x() + (bar.get_width() / 2.0)
                y_pos = val + barlabel_offset
                barlbl = bar_labeler(g_name, val_i, val)
                ax.text(x_pos, y_pos, barlbl, ha="center", va="bottom",
                        fontsize=label_fontsize)
    if legend:
        ax.legend([bars[k][0] for k in sorted_k], sorted_k)
    #
    ax.set_xticks(group_centers)
    if x_labels:
        ax.set_xticklabels(sorted_k)
    else:
        ax.set_xticklabels()
    return bars, group_centers