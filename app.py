from flask import Flask, render_template  # 템플릿 리턴

app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

@app.route('/')
def hello():
    req = requests.get("https://www.nate.com/")

    soup = BeautifulSoup(req.text, 'html.parser')

    for i in soup.select("#olLiveIssueKeyword"):
        print(i.find("a").text)

    return render_template("index.html")


@app.route('/about')
def about():
    return "여기는 about 입니다."


if __name__ == '__main__':
    app.run(debug=True)
