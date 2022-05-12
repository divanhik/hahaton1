from requests import post
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("first.html", title="Главная страница", trains=get_data())


def time(tm):
    new = tm.split(':')
    return int(new[0]) * 60 + int(new[1])


def normal(sp):
    result = list()
    for i in sp:
        new = []
        for j in i:
            if '-' not in j: new.append(j)
            else:
                name = j.split('-')
                for n in name:
                    new.append(' '.join(n.split('+')))
        result.append(new)
    return result


def get_data():
    #req = post('https://inf2086.ru/trains_timetable_api/timetable', data='340yk034k4f').text
    req = open('2.txt', 'r', encoding='UTF-8').read()
    data = [x.split() for x in req.split('\n')]
    if data[-1] == []: del data[-1]
    data = sorted(data, key=lambda x: time(x[3]))
    return normal(data)


app.run('', 8092, debug=True)