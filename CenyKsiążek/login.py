#!/usr/bin/env python

import mechanicalsoup


def login(email, password):

    browser = mechanicalsoup.Browser(soup_config={'features':'html.parser'})
    loginPage = browser.get('https://ebooki.swiatczytnikow.pl/mojealerty')
    form = loginPage.soup.find_all('form')[0]
    form.find('input', {'name':'email'})['value'] = email
    form.find('input', {'name':'password'})['value'] = password
      
    
    response = browser.submit(form, loginPage.url)
    
    strona = response.text
    
    return strona

    
