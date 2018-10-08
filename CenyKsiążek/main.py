#!/usr/bin/env python
# -*- coding: utf-8 -*-
import create_database 
#import add_book_to_database

import pandas as pd
import plot

import add_book_to_database as add_to_db

import os

def prepare_plot():
            
        x_col = df2['date']
        y_col= df2['prices']
        first_title = df2.loc[1,'titles']

        plot.createPlot(x_col, y_col, first_title, id) 
            
print('Witaj')
print('###############')

while id != 't':  
    
    print('Wciśnij: \n 1 aby zobaczyc dostepne tytuly \n 2 aby zobaczyc wszystkie dane  \n 3 aby dodac nowe dane do bazy')
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
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print('                DOSTĘPNE KSIĄŻKI')
        print(df)
        print("------------------------------------------------------")
        title_list = df['nazwa'].tolist()
        index_list = df.index.get_values()   
        
# ##################################################
        print('Wybierz: \n numer książki z powyższej listy \n 0 aby wyswietlic wykresy dla wszystkich książek ')
        id = input('')
        id2 = int(id)
                 
        if id2 in index_list:
            wybrany_tytul = df.loc[id2,'nazwa']
    
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
            prepare_plot()      
              
        elif id2 == 0:
            for title in title_list:
                query = '''
                        SELECT  titles, prices, date
                            FROM Titles 
                        INNER JOIN Prices
                            ON Titles.id=Prices.id
                        INNER JOIN AddDate
                            ON AddDate.id=prices.id 
                        WHERE Titles.titles = \''''+ title +'''\' ''' # / znak modyfikacji
                    
                df2 = pd.DataFrame(pd.read_sql(query,create_database.engine) )
                df2.index = df2.index + 1                       
                print (df2)
        
                prepare_plot()
                
            import matplotlib.pyplot as plt
            plt.show()   
        else:
            print('')
            print('Posiadasz tylko', len(index_list),'książek')
            print('Wybierz numer z zakresu od 1 do', len(index_list),'przypisany do Twojej książki zgdonie z listą.') 
            print('')
# ##################################################                   
    elif ok == '2':
    
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
        
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print (df)
    
    elif ok == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        add_to_db.get_date()  
        add_to_db.login_to_Account()   
        add_to_db.get_data_from_webpage() 
    
    

    
    id = input('czy zakonczyc? t/n ')
    os.system('cls' if os.name == 'nt' else 'clear')
    
print("Koniec")
