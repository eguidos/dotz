from DAO import conf, tables
from model.fact.bill import Billing
from model.dimension.price import Pricing
from model.dimension.components import Components
from commom import log, utils
from sqlalchemy import create_engine


def run_price(data):
    price = Pricing(data).run()
    return price


def run_bill(data):
    bill = Billing(data).run()
    return bill


def run_components(data):
    components = Components(data).run()
    return components


class Execution:
    try:
        log.logging.warning("Criando Componentes necessários")

        def __init__(self):
            self.cursor = conf.db.cursor()
            self.engine = create_engine('mysql://root:admin@localhost/industry')

        def create_db(self):
            self.cursor.execute(utils.create_db())

        def set_db(self):
            self.cursor.execute(utils.set_db())

        def create_table(self):
            try:
                self.cursor.execute(tables.create_price())
                self.cursor.execute(tables.create_components())
                self.cursor.execute(tables.create_bill())
            except ConnectionError:
                log.logging.warning('Não foi possível criar as tabelas.')

        def insert_data_bill(self, data):
            bill = run_bill(data)
            bill.to_sql('bill', con=self.engine, if_exists='replace', index=False)

        def insert_data_price(self, data):
            price = run_price(data)
            price.to_sql('price', con=self.engine, if_exists='replace', index=False)

        def insert_data_components(self, data):
            components = run_components(data)
            components.to_sql('components', con=self.engine, if_exists='replace', index=False)

    except ConnectionError:
        log.logging.error("Não realizar a conexão ")
    finally:
        log.logging.warning("Arquivos carregados, preparando inserções.")
