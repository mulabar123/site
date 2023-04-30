from flask import Flask, render_template, url_for, redirect, request
from db import *
import os

folder = os.getcwd()
create_table()

app = Flask(__name__)

@app.route('/')
def indexMain():
    return render_template('index.html')

@app.route('/posts')
def indexPosts():
    data = get_posts()
    return render_template('posts.html', data=data)

@app.route('/add_post', methods=['GET', 'POST']) # Страница добавления поста
def addPost():
    if request.method == 'POST': # Если метод POST
        # Получаем заголовок и текст
        title = request.form['title']
        content = request.form['text']
        add_post(title, content) # Добавляем в БД
        return redirect(url_for('indexPosts')) # Перебрасываем на страницу с постами
    return render_template('addpost.html') # Возвращаем поле ввода

if __name__ == "__main__":
    app.run()