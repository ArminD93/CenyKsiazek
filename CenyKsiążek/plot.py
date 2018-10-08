#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')


from matplotlib.pyplot import figure



def createPlot(x_col, y_col, title, id):
    

    figure(num=None, figsize=(1, 1), dpi=80)
    
    plt.rcParams['figure.figsize'] = 15, 15


    plt.gca()

    plt.gcf().autofmt_xdate()

    x = x_col
    y = y_col

    y=y.astype(float)

    plt.xlabel('data')
    plt.ylabel('cena')
    plt.title(title)

    plt.plot(x, y,)

    if id != '0':
        plt.show()
 
        
        
        
        
        
        
        
'''
def createPlot(x_col, y_col, title, index_list):
    
   

    fig = plt.figure()
    
    list = index_list
    

        
    for i in list:
        
        x = x_col
        y = y_col
        y=y.astype(float)
        ax = plt.subplot(4, 4, i)
        plt.plot(x, y)
        
        i+=1
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
        plt.tight_layout(pad=1, w_pad=1, h_pad=1.0)
            
    
        plt.title(title)            
 '''   
    
  

