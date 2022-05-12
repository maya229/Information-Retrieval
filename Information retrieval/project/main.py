from flask import Flask, redirect, url_for, render_template, request

import string, random

app = Flask(__name__)
def generate():
    char = ['a', 'b', 'c', 'd', 'e', 'f']
    for i in range(1, 11):
        file = open('g/g%i' % i, 'w')
        file.write(' '.join(random.choice(char)for i in range(0,random.randint(5,20))))
        file.close()

@app.route('/')
def main():
    generate()
    return render_template('main.html')
@app.route('/generate')
def genbutton():
    generate()
    return render_template('main.html')


@app.route('/Smodel', methods=['POST'])
def data():
    dic = {'g1': 0, 'g2': 0, 'g3': 0, 'g4': 0, 'g5': 0, 'g6': 0, 'g7': 0, 'g8': 0, 'g9': 0, 'g10': 0}
    product1 = [] 

    wa = float(request.form["q1"])
    wb = float(request.form["q2"])
    wc = float(request.form["q3"])
    wd = float(request.form["q4"])
    we = float(request.form["q5"])
    wf = float(request.form["q6"])
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    all = 0

    for i in range(1, 11):
        file = open('g/g%i' % i, 'r')
        l = file.readline()
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0

        for i in range(len(l)):
            if l[i] == 'a':
                a = a + 1
            if l[i] == 'b':
                b = b + 1
            if l[i] == 'c':
                c = c + 1
            if l[i] == 'd':
                d = d + 1
            if l[i] == 'e':
                e = e + 1
            if l[i] == 'f':
                f = f + 1

        ca = (a / len(l)) * wa
        cb = (b / len(l)) * wb
        cc = (c / len(l)) * wc
        cd = (d / len(l)) * wd
        ce = (e / len(l)) * we
        cf = (f / len(l)) * wf
        product1.append(ca + cb + cc + cd + ce + cf)

    dic = {'g1': product1[0], 'g2': product1[1], 'g3': product1[2], 'g4': product1[3], 'g5': product1[4], 'g6': product1[5], 'g7': product1[6],
           'g8': product1[7], 'g9': product1[8], 'g10': product1[9]}

    sorted_dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=True)}

    return render_template("result.html", data=sorted_dic) 


if __name__ == "__main__":
    app.run(debug=True)