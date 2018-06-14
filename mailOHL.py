#!/usr/bin/env python3

import requests
import texttable as tt
import smtplib
import email.message
import operator
from bs4 import BeautifulSoup
res = requests.get('https://docs.google.com/spreadsheets/d/1rBV78LxZcu2J2L5rCEaBPAujnY4NJEbxLMqsfQXxh0g/pubhtml/sheet?headers=false&gid=0').text
res2 = requests.get('https://zerodha.com/margin-calculator/Equity/').text
soup = BeautifulSoup(res, 'html.parser')
soup2= BeautifulSoup(res2, 'html.parser')
heading = [soup.tbody.tr.contents[j].text for j in {1,7,9,5}]
heading.append('ZERODHA')
html = """<html><table class="sortable" border="1">
           <thead>
            <tr>"""
for headings in heading:
    html +="<th>{}</th>".format(headings)
html +="</tr></thead><tbody>"
tab_conts=[]
for i in soup.tbody.contents:
    if i.contents[9].text == 'OPEN=HIGH' or i.contents[9].text == 'OPEN=LOW' or i.contents[1].text == 'NIFTY' or i.contents[1].text == 'BANKNIFTY':
        contents = [i.contents[j].text for j in {1,7,9,5}]
        stock=contents[0]
        st=stock+':EQ'
        for row in soup2.tbody.findAll('tr'):
            for td in row.findAll('td'):
                if td.text == st:
                    contents.append(td.findNext(attrs='mis').text.strip())
        tab_conts.append(contents)
tabnew = sorted(tab_conts, key=operator.itemgetter(3))
for row in tabnew:
    html +="<tr>"
    for item in row:
        html +="<td>{}</td>".format(item)
    html +="<tr>"
html += "</table></html>"
msg = email.message.Message()
msg['Subject'] = 'OHL'
msg['To'] = 'chijumelveettil@gmail.com'
password = "9567076828Cc#"
msg['From'] = 'chijumel@gmail.com'
msg.add_header('Content-Type', 'text/html')
msg.set_payload(html)
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(msg['From'], password)
smtpserver.sendmail(msg['From'], [msg['To']], msg.as_string())
smtpserver.quit()
