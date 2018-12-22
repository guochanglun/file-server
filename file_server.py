from flask import Flask, render_template, request, send_file, session, redirect, url_for
import os
import time
from urllib import parse


Base_Dir = 'D:\\data\\小项目\\file server\\files'

app = Flask(__name__, static_folder=Base_Dir)
app.secret_key = 'd2da3#fasd3@w4etAsdw$w43tAr3'

@app.route('/')
def index():
    if session.get('login', None) != None:
        return redirect(url_for('files'))

    return render_template("login.html")


def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if session.get('login', None) != None:
        return redirect(url_for('files'))
    if request.method == 'get': return redirect(url_for('index'))
    name = request.form.get('name')
    pwd = request.form.get('pwd')
    if name == 'zhazha' and pwd == 'zhazha':
        session['login'] = True
        return redirect(url_for('files'))
    else:
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    del session['login']
    return redirect(url_for('index'))


@app.route('/f')
def files():
    if session.get('login', None) == None:
        return redirect(url_for('index'))
    path = request.args.get('p', Base_Dir)
    path = parse.unquote(path)
    print(path)
    if os.path.isdir(path):
        file_list = os.listdir(path)
        files = []
        for file in file_list:
            file_path = os.path.join(path, file)
            if os.path.isdir(file_path):
                type = 'd'
            else:
                type = 'f'
            files.append({
                    "name": file,
                    "path": parse.quote(file_path),
                    "type": type,
                    "size": '%.5f' % (os.path.getsize(file_path) / 1024.0),
                    "ctime": TimeStampToTime(os.path.getctime(file_path))
                })
        return render_template("files.html", files=files)
    else:
        return send_file(path)


if __name__ == '__main__':
    app.run(port=9527, debug=True)