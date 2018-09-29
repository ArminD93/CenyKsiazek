#!/usr/bin/env python
# coding: utf-8
import create_database 
#import add_book_to_database

import pandas as pd
import plot

import add_book_to_database as add_to_db

print('Witaj')
print('###############')

ok = input('Wciśnij: \n 1 aby zobaczyc listę książek \n 2 aby dodac nowe dane do bazy ')

if ok == '1':
    
    query = '''
            SELECT  titles, prices, date
            FROM Titles 
            INNER JOIN Prices
                ON Titles.id=Prices.id
            INNER JOIN AddDate
                ON AddDate.id=prices.id 
        '''
    df = pd.DataFrame(pd.read_sql(query,create_database.engine) )
    df.index = df.index + 1

    print (df)
    
elif ok == '2':
        
        
    
        
        add_to_db.get_date()
        
        add_to_db.login_to_Account()
    
        
        add_to_db.get_data_from_webpage()
    
    
id = input('Wybierz id książki: ')


query = '''
            SELECT  titles, prices, date
            FROM Titles 
            INNER JOIN Prices
                ON Titles.id=Prices.id
            INNER JOIN AddDate
                ON AddDate.id=prices.id 
            WHERE Titles.titles = (SELECT titles FROM Titles WHERE Titles.id= '''+id+''')
            
            AND (Titles.id !=''' +id + '''
            OR Titles.id =''' +id+''')'''
        
df2 = pd.DataFrame(pd.read_sql(query,create_database.engine) )
df2.index = df2.index + 1
print (df2)

x_col = df2['date']
y_col= df2['prices']

plot.createPlot(x_col, y_col)
