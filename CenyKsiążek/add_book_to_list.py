#!/usr/bin/env python


from bs4 import BeautifulSoup as soup  # HTML data structure
import login
import re
import datetime
import getpass




now = datetime.datetime.now()

date = now.strftime("%d.%m.%Y")

email = input("Podaj email do konta: ")
password = getpass.getpass("Podaj hasło do konta: ")


page_soup = soup(login.login(email, password), "html.parser")


containers = page_soup.findAll("tbody")


filename = "ksiazki.csv"

headers = "nazwa,cena[zl],dane z dnia \n"


#f = open(out_filename, "a")
#f.write(headers)


try:
    f = open(filename, "a")
  
except IOError:
    print('File is not accessible')

    f.writelines(headers)
    print("dopisanie naglowkowa")


for container in containers:

    book = container.findAll("td", {"class": ""})
    
    nazwa1 = book[0].text.strip()
    nazwa = re.sub(r'\s\s+', '', nazwa1)
    cena1 = book[1].text.strip()
    cena = cena1[3:8]
    #data = book[4].text.strip()
    data = date
    

    print("nazwa: " + nazwa + "\n")
    print("cena: " + cena + "\n")
    print("data: " + data + "\n")    
 

    f.write(nazwa + ", " + cena + ", " + data.replace(",", "|") + "\n")
f.write(" "+ "\n")   

f.close() 
