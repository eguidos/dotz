import os


def create_db():
    create = "CREATE DATABASE IF NOT EXISTS industry;"
    return create


def set_db():
    set = "use industry;"
    return set


def get_path(path):
    return os.path.abspath(f'../dotz/data/{path}')