import requests
from bs4 import BeautifulSoup

def ent():
    req = requests.get("https://entertain.naver.com/home")

    soup = BeautifulSoup(req.text, 'html.parser')

    list_ent = []
    list_ent_href = []

    for i in soup.select("#ranking_news > div > div.rank_lst > ul > li"):
        list_ent.append (i.find("a").text)
        list_ent_href.append(i.find("a")["href"])

    return list_ent, list_ent_href


#오늘의 유머
def today():
    req = requests.get("http://www.todayhumor.co.kr/board/list.php?table=bestofbest")

    soup = BeautifulSoup(req.text, 'html.parser')

    list_today = []
    list_today_href = []

    for i in soup.find_all("td", class_="subject"):
        list_today.append(i.text)
        list_today_href("http://www.todayhumor.co.kr" + i.find("a")["href"])

    return list_today, list_today_href


#클리앙
def clien():
    req = requests.get("https://www.clien.net/service/recommend")

    soup = BeautifulSoup(req.text, 'html.parser')

    list_clien  = []
    list_clien_href = []

    for i in soup.find_all("span", class_="subject_fixed"):
        list_clien.append(i.text)

    for i in soup.find_all("a", class_="list_subject"):
        list_clien_href.append("https://www.clien.net" + i["href"])

    return list_clien, list_clien_href