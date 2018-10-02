#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup as soup  # HTML data structure
import re
import datetime
import login
import getpass

from create_database import *




def get_date():
    
    global date
    now = datetime.datetime.now()
    date = now.strftime("%d.%m.%Y")
    return date
    

def login_to_Account():
    
    global email
    global password
    
    FLG = False
    
    while FLG == False:
        email = input("Podaj email do konta: ")
    
        verify_mail = re.match(r'^.+@[^.].*\.[a-z]{2,10}$', email)
        
        if verify_mail : 
            FLG = True 
            print("Email prawidłowy")
        
            password = getpass.getpass("Podaj hasło do konta: ")
    
            return email, password
        else:  
            print("Email nieprawidłowy")
    

      
def get_data_from_webpage():

    page_soup = soup(login.loginToAccount(email, password), "html.parser")

    containers = page_soup.findAll("tbody")
  
    for container in containers:
        book = container.findAll("td", {"class": ""})
    
        nazwa1 = book[0].text.strip()
        nazwa = re.sub(r'\s\s+', '', nazwa1)
    
        nazwa = Titles(titles= nazwa)
        session.add(nazwa)
    
        cena1 = book[1].text.strip()
        cena = cena1[3:8]

        cena = Prices(prices= cena)
        session.add(cena)
    
        data = date
    
        data = AddDate(date= data)
        session.add(data)
       
    session.commit()

    print('Dane zostały dodane do bazy danych.')
    session.close()


