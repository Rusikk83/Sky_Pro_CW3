from flask import Flask, request, render_template, send_from_directory, jsonify
from utils.utils import *
import logging

"""Подключение и настройка логера"""
api_logger = logging.getLogger("api")
api_logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("api.log")
api_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler.setFormatter(api_formatter)
api_logger.addHandler(file_handler)

app = Flask(__name__)

"""Загруска списка постов и коментариев"""
posts = get_posts_all()
comments = get_comments_all()

app.config['JSON_AS_ASCII'] = False

"""Представление для страницы со списком всех постов"""


@app.route("/")
def page_index():
    return render_template("index.html", items=posts)


"""Представление для результата поиска постов по строке вхождения"""


@app.route("/search")
def page_search():
    find_text = request.args.get("s")
    posts_search = search_in_posts(posts, find_text)
    return render_template("search.html", posts=posts_search[0:10], search_count=len(posts_search))


"""Представление для отображения полной информации поста по идентификатору"""


@app.route("/post/<int:post_id>")
def page_post(post_id):
    post = get_post_by_pk(posts, post_id)
    comments_of_post = get_comments_by_post_id(comments, posts, post_id)
    return render_template("post.html", post=post, comments=comments_of_post)


"""Представление для отображения постов пользователя по его имени"""


@app.route("/users/<user_name>")
def page_user_post(user_name):
    user_posts = get_posts_by_user(posts, user_name)
    return render_template('user-feed.html', posts=user_posts)


"""Представление для доступа к файлам"""


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


"""обработчик ошибки обращения к несуществующей странице"""


@app.errorhandler(404)
def error_404(error):
    return "Запрошенная страница не существует", 404


"""обработчик ошибки сервера"""


@app.errorhandler(500)
def error_500(error):
    return "Сервер не доступен, попробуйте позже", 500


"""Представление для обработки запросов api для получения списка всех постов"""


@app.route("/api/posts")
def get_posts_api():
    api_logger.info("/api/posts")
    return jsonify(posts)


"""Представление для обработки запросов api для поста по идентификатору"""


@app.route("/api/posts/<int:post_id>")
def get_post_api(post_id):
    api_logger.info(f"/api/posts/{post_id}")
    post = get_post_by_pk(posts, post_id)
    return jsonify(post)


if __name__ == "__main__":
    app.run()
