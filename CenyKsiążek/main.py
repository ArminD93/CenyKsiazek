#!/usr/bin/env python
# -*- coding: utf-8 -*-
import create_database 
#import add_book_to_database

import pandas as pd
import plot

import add_book_to_database as add_to_db

print('Witaj')
print('###############')

while id != 't':  
    print(('Wciśnij: \n 1 aby zobaczyc dostepne tytuly \n 2 aby dodac nowe dane do bazy \n 3 aby zobaczyc wszystkie dane '))
    ok = input('')
    print("------------------------------------------------------")


    if ok == '1':
    

        query = '''
                SELECT  DISTINCT titles
                FROM Titles 
                '''
        df = pd.DataFrame(pd.read_sql(query,create_database.engine) )
        df.index = df.index + 1
        df.columns = ['nazwa']
        
        print('                DOSTĘPNE KSIĄŻKI')
        print(df)
            
    elif ok == '2':
    
        add_to_db.get_date()  
        add_to_db.login_to_Account()   
        add_to_db.get_data_from_webpage()
        
    elif ok == '3':
    
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
    
    
    
    
    id = input('Wybierz numer książki: ')
    id2 = int(id)
                     
    wybrany_tytul = df.loc[id2,'nazwa']
    
    print("wybrany_tytul: ", wybrany_tytul, type(wybrany_tytul))
    print("")
    
   
    

    query = '''
                SELECT  titles, prices, date
                    FROM Titles 
                INNER JOIN Prices
                    ON Titles.id=Prices.id
                INNER JOIN AddDate
                    ON AddDate.id=prices.id 
                WHERE Titles.titles = \''''+ wybrany_tytul+'''\' ''' # / znak modyfikacji
        
    df2 = pd.DataFrame(pd.read_sql(query,create_database.engine) )
    df2.index = df2.index + 1
    print (df2)

    x_col = df2['date']
    y_col= df2['prices']

    first_title = df2.loc[1,'titles']

    plot.createPlot(x_col, y_col, first_title)
    
    id = input('czy zakonczyc? t/n ')
    
print("Koniec")
