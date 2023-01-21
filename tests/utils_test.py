import pytest
from utils.utils import *
from data_json import *


def test_load_posts():
    assert len(get_posts_all()) == 8


def test_load_comments():
    assert len(get_comments_all()) == 20


def test_exists_file_posts():
    with pytest.raises(FileNotFoundError):
        get_posts_all('no_path')


def test_exists_file_comments():
    with pytest.raises(FileNotFoundError):
        get_comments_all('no_path')


def test_get_posts_by_user_leo():
    assert len(get_posts_by_user(test_posts, "LEO")) == 2


def test_get_posts_by_user_noname():
    assert get_posts_by_user(test_posts, "no_name") == []


def test_get_comments_by_post_id_1():
    assert len(get_comments_by_post_id(test_comments, test_posts, 1)) == 4


def test_get_comments_by_post_id_nopost():
    with pytest.raises(ValueError):
        get_comments_by_post_id(test_comments, test_posts, 99)


def test_search_for_posts():
    assert len(search_in_posts(test_posts, "А")) == 8


def test_search_for_posts_type():
    assert type(search_in_posts(test_posts, "вал")) == list


def test_search_for_posts_null():
    assert search_in_posts(test_posts, "giojijoijljij") == []


def test_get_post_by_pk():
    assert get_post_by_pk(test_posts, 1)['pk'] == 1



def test_get_post_by_pk_value():
    with pytest.raises(ValueError):
        get_post_by_pk(test_posts, "1")

