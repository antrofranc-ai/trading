#!/usr/bin/env python3

import requests
#import texttable as tt
import smtplib
import email.message
import operator
from tabulate import tabulate
from bs4 import BeautifulSoup
res = requests.get('https://docs.google.com/spreadsheets/d/1rBV78LxZcu2J2L5rCEaBPAujnY4NJEbxLMqsfQXxh0g/pubhtml/sheet?headers=false&gid=0').text
res2 = requests.get('https://zerodha.com/margin-calculator/Equity/').text
soup = BeautifulSoup(res, 'html.parser')
soup2= BeautifulSoup(res2, 'html.parser')
heading = [soup.tbody.tr.contents[j].text for j in {1,7,9,5}]
heading.append('ZERODHA')
niftyl=''
for i in soup.tbody.contents:
    if i.contents[1].text == 'NIFTY' or i.contents[1].text == 'BANKNIFTY':
        nifty=[i.contents[j].text for j in {1,7,9,5}]
        niftyl += nifty[0] + ' ' + nifty[3] + '\n'
#print(niftyl)
tab_conts=[]
for i in soup.tbody.contents:
    if i.contents[9].text == 'OPEN=HIGH' or i.contents[9].text == 'OPEN=LOW':
        contents = [i.contents[j].text for j in {1,7,9,5}]
        stock=contents[0]
        st=stock+':EQ'
        for row in soup2.tbody.findAll('tr'):
            for td in row.findAll('td'):
                if td.text == st:
                    contents.append(td.findNext(attrs='mis').text.strip())
        tab_conts.append(contents)
tabnew=[]
tabnew.append(heading)
tabnew += sorted(tab_conts, key=operator.itemgetter(3), reverse=True)
mtable = tabulate(tabnew[1:], headers=tabnew[0], tablefmt="html", floatfmt='g', numalign='decimal', stralign='center', missingval='')
mtable = '<html>' + niftyl + mtable + '<html>'
mtable = mtable.replace('<table>', '<table border=1>')
msg = email.message.Message()
msg['Subject'] = 'OHL'
msg['To'] = 'chijumelveettil@gmail.com'
password = "9567076828Cc#"
msg['From'] = 'chijumel@gmail.com'
msg.add_header('Content-Type', 'text/html')
msg.set_payload(mtable)
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(msg['From'], password)
smtpserver.sendmail(msg['From'], [msg['To']], msg.as_string())
smtpserver.quit()
