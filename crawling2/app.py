from flask import Flask, render_template, request

import requests
from bs4 import BeautifulSoup

from openpyxl import Workbook

write_wb = Workbook()           #excel
write_ws = write_wb.active

from selenium import webdriver  #셀레니움 import 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def result():

    keyword = request.form['input1']
    page = request.form['input2']

    #https://search.daum.net/search?nil_suggest=btn&w=news&DA=PGD&q=%EC%95%88%EB%85%95&p=1 

    daum_list = []

    for i in range(1,int(page)+1):

        req = requests.get("https://search.daum.net/search?nil_suggest=btn&w=news&DA=PGD&q=" + keyword + "&p=" + str(i) )
        soup = BeautifulSoup(req.text,  'html.parser')

        for i in soup.find_all("a", class_="tit_main fn_tit_u" ):
            daum_list.append(i.text)

    for i in range(1,len(daum_list) + 1 ):
        write_ws.cell(i,1,daum_list[i-1])
             
    write_wb.save("static/result.xlsx")


    return render_template("result.html", daum_list = daum_list)



@app.route('/naver_shopping')
def naver_shopping():
     
    driver  = webdriver.Chrome('./chromedriver')

    #driver.implicitly_wait(3)

    driver.get('https://search.shopping.naver.com/search/all?query=%EB%A7%A5%EB%B6%81')

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    for i in soup.select('#__next > div > div.style_container__UxP6u > div.style_inner__i4gKy > div.style_content_wrap__Cdqnl > div.style_content__xWg5l > ul > div > div'):
        print(i.find('a',class_='basicList_link__JLQJf').text)
    
    return render_template('shopping.html')



if __name__ == '__main__':
    app.run()