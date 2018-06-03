def margin(stock):
    st=stock+':EQ'
    for row in soup.tbody.findAll('tr'):
        for td in row.findAll('td'):
            if td.text == st:
                print(td.text)
                print(td.findNext(attrs='mis').text.strip())
