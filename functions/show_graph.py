import matplotlib.pyplot as plt
from functions.df_tools import *
import pandas as pd

def bar_plot(ax, data, group_stretch=0.8, bar_stretch=0.95,
             legend=True, x_labels=True, label_fontsize=8,
             colors=None, barlabel_offset=1,
             bar_labeler=lambda k, i, s: str(round(s, 3))):

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

def show_graph(seleted_graph):
    if seleted_graph == 1:
        f = readTxt('user.txt')
        print("Amount of people of Registrants in the same age.")
        data = f.groupby(['age']).size().reset_index(name='counts')
        df = pd.DataFrame(data ,columns=['age','counts'])
        df.plot(x ='age', y='counts', kind = 'bar')
        plt.show()
    elif seleted_graph == 2: 
        f = readTxt('schedual.txt')
        print("Amount of people of Reschedule on the same day.")
        data = f.groupby(['date']).size().reset_index(name='counts')
        df = pd.DataFrame(data ,columns=['date','counts'])
        df.plot(x ='date', y='counts', kind = 'bar')
        plt.title("Amount of people of Reschedule on the same day.")
        plt.show()
    elif seleted_graph == 3: 
        f = readTxt('schedual.txt')
        print("Amount of reservation vaccines at the same Hospital.")
        data = f.filter(items=['Vaccine name', 'location']).groupby(['Vaccine name', 'location']).size().reset_index(name='counts')
        data.pivot(index='location', columns='Vaccine name', values='counts').plot(kind='bar')
        plt.title("Amount of reservation vaccines at the same Hospital.")
        plt.show()
    elif seleted_graph == 4: 
        vaccine = readTxt('vaccine.txt')
        user = readTxt('user.txt')
        print("Amount of people of Registrants by age.")
        vaccine_by_age = user.join(vaccine, lsuffix='_caller', rsuffix='_other')
        vaccine_by_age = vaccine_by_age.filter(items=['first dose', 'age']).groupby(['first dose', 'age']).size().reset_index(name='counts')
        vaccine_by_age.pivot(index='age', columns='first dose', values='counts').plot(kind='bar')
        plt.title("Amount of people of Registrants by age.")
        plt.show()
    elif seleted_graph == 5: 
        vaccine = readTxt('vaccine.txt')
        print("Amount of people of Registrants with vaccine.")
        vaccine = vaccine.groupby(['first dose', 'second dose']).size().reset_index(name='counts')
        vaccine.plot(x ='first dose', y='counts', kind = 'bar')
        plt.show()


def main():
    print("Show graph")
    seleted_graph = int(input("Select graph 1-10\n: "))
    show_graph(seleted_graph)
    # print(graph)

if __name__ == '__main__':
    main()
    