import json


def get_posts_all(path="data/posts.json"):
    """Загружает посты из файла в список"""
    with open(path, "r", encoding="UTF-8") as file:
        data = file.read()
        posts_all = json.loads(data)
        return posts_all


def get_comments_all(path="data/comments.json"):
    """Загружает комментарии из файла в спимок"""
    with open(path, "r", encoding="UTF-8") as file:
        data = file.read()
        comments_all = json.loads(data)
        return comments_all


def get_posts_by_user(posts_list, user_name):
    """возвращает посты определенного пользователя и пустой список,
     если у пользователя нет постов"""
    user_posts = []
    for el in posts_list:
        if el["poster_name"].lower() == user_name.lower():
            user_posts.append(el)

    return user_posts



def get_comments_by_post_id(comments_list, posts_list, post_id):
    """возвращает комментарии определенного поста.
     Функция должна вызывать ошибку ValueError если такого поста нет
      и пустой список, если у поста нет комментов"""
    comments_of_post = []

    post_exists = False
    for el in posts_list:
        if el["pk"] == post_id:
            post_exists = True
            break

    if not post_exists:
        raise ValueError("Post not exists")

    for el in comments_list:
        if el['post_id'] == post_id:
            comments_of_post.append(el)
    return comments_of_post


def search_in_posts(posts_list, query):
    """Возвращает список постов по вхождению строки, или пустой список если посты не найдены"""
    find_posts = []
    for el in posts_list:
        if query.lower() in el["content"].lower():
            find_posts.append(el)
    return find_posts


def get_post_by_pk(posts_list, pk):
    """Возвращает данные поста по номеру, или исключение ValueError если поста с таким номером нет"""
    if type(pk) != int:
        raise ValueError("Post not exists")

    for el in posts_list:
        if el["pk"] == pk:
            return el
    raise ValueError("Post not exists")
