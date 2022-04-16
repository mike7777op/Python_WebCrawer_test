# encoding:utf-8
import urllib.request as req
from bs4 import BeautifulSoup


def funtion_converter():
    url = 'https://doc.wikimedia.org/mediawiki-core/REL1_31/php/ZhConversion_8php_source.html'
    request = req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode('utf-8')

    root = BeautifulSoup(data,'html.parser')

    lines = root.find_all('div',class_='line')

    a = []
    for i in lines:
        stringliteral = i.find('span',class_='stringliteral')
        
        
        if stringliteral is not None:
            
            for j in i.find_all('span',class_='lineno'):
                # 把lineno的數值拿掉
                j.decompose()
                text = i.text
                text = text.replace('=>','')
                text = text.replace(',','')
                text = text.replace("'",'')
                text = text.replace(' ','')
                text= ''.join(text.split())
                a.append(text)
    return a


def converter():
    a = funtion_converter()
    v = []
    for i in a:
        if len(i)==2:
            v.append(i)
    return v
