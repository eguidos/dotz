import os
from utils import log


def create_db():
    create = "CREATE DATABASE IF NOT EXISTS industry;"
    return create


def set_db():
    set = "use industry;"
    return set


def get_path(path):
    return os.path.abspath(f'../dotz/data/{path}')


def data_values(tbname, df):
    log.logging.warning(f"Dados a serem inseridos na tabela {tbname} \n \t {df}")

def data_error():
    log.logging.warning(f"O arquivo necessário não foi encontrado")

def not_exists(file):
    log.logging.error(f"O arquivo necessário não foi encontrado")

