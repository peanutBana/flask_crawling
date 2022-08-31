from flask import Flask, render_template  # 템플릿 리턴

app = Flask(__name__)

import crawling

@app.route('/')
def hello():
    
    list_ent, list_ent_href = crawling.ent()
    list_today, list_today_href = crawling.today()
    list_clien, list_clien_href = crawling.clien()
        
    return render_template("index.html",ent=list_ent, 
                                        today=list_today, 
                                        clien=list_clien,
                                        ent_href = list_ent_href,
                                        today_href = list_today_href,  
                                        clien_href = list_clien_href,
                                        ent_len = len(list_ent),
                                        today_len = len(list_today),
                                        clien_len = len(list_clien)
                                        )  


@app.route('/about')
def about():
    return "여기는 about 입니다."


if __name__ == '__main__':
    app.run(debug=True)
