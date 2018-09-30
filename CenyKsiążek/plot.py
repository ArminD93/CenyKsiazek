#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')


from matplotlib.pyplot import figure
figure(num=None, figsize=(1, 1), dpi=80)


def createPlot(x_col, y_col, title):


    plt.rcParams['figure.figsize'] = 15, 10


    plt.gca()

    plt.gcf().autofmt_xdate()

    x = x_col
    y = y_col

    y=y.astype(float)

    plt.xlabel('data')
    plt.ylabel('cena')
    plt.title(title)

    plt.plot(x, y,)


    plt.show()