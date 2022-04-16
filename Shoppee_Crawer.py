from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from Converter import converter
import time

# 使用selenium進行爬蟲
def selenium():

    PATH = Service("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")

    driver = webdriver.Chrome(service=PATH)

    driver.get('https://shopee.tw/%E5%A8%9B%E6%A8%82%E3%80%81%E6%94%B6%E8%97%8F-cat.11041645')


    product_title_list = []

    # 因為網頁為Ajax非同步，所以自動滾輪去撈資料
    js="var q=document.documentElement.scrollTop=400"  
    driver.execute_script(js)

    products_title = driver.find_elements(by=By.CLASS_NAME,value='ZG__4J')

    for product_title in products_title:
        product_title_list.append(product_title.text)
        # product_title.text
    time.sleep(5)


    js="var q=document.documentElement.scrollTop=1400"  
    driver.execute_script(js)

    products_title = driver.find_elements(by=By.CLASS_NAME,value='ZG__4J')

    for product_title in products_title:
        product_title_list.append(product_title.text)
        # product_title.text
    time.sleep(5)



    js="var q=document.documentElement.scrollTop=2400"  
    driver.execute_script(js)


    products_title = driver.find_elements(by=By.CLASS_NAME,value='ZG__4J')

    for product_title in products_title:
        product_title_list.append(product_title.text)
        # product_title.text
    time.sleep(5)


    js="var q=document.documentElement.scrollTop=3400"  
    driver.execute_script(js)

    products_title = driver.find_elements(by=By.CLASS_NAME,value='ZG__4J')

    for product_title in products_title:
        product_title_list.append(product_title.text)
        # product_title.text
    time.sleep(5)

    js="var q=document.documentElement.scrollTop=4400"  
    driver.execute_script(js)

    products_title = driver.find_elements(by=By.CLASS_NAME,value='ZG__4J')

    for product_title in products_title:
        product_title_list.append(product_title.text)
        # product_title.text
    time.sleep(5)


    price_list=[]
    products_price = driver.find_elements(by=By.CLASS_NAME,value='_3_FVSo')
    for product_price in products_price:
        price_list.append(product_price.text)


    driver.quit()
    
    return product_title_list, price_list

def translate(string,a):
    new_string = ''
    for i in string:
        b = [x for x in a if i in x]
        if b:
            # 把另外一個字刪除並重新組合
            less_string = ''.join(z for z in b[0] if z not in i)
            new_string+=less_string
        # 查詢不到的值，原封不動的加回去
        else:
            new_string+=i
    return new_string



def main():

    product_title_list,price_list = selenium()

    # 去除重複的值
    product_title_set_list = list(set(product_title_list))
    # 由於使用set會打亂原本的順序，使用sort排序回原來的index
    product_title_set_list.sort(key=product_title_list.index)
    item_len = len(product_title_set_list)

    translate_list = set(converter())

    i = 0
    while i < item_len:
        # translate(product_title_set_list[i],translate_list)
        print('Or_Product:',product_title_set_list[i])
        print('Con_Product:',translate(product_title_set_list[i],translate_list))
        print('Price:',price_list[i])
        i+=1

if __name__ == "__main__":
    main()
