from cfs.exect import Execution
from utils import utils
from utils import log
bill = utils.get_path('./bill_of_materials.csv')
price = utils.get_path('./price_quote.csv')
comp = utils.get_path('./comp_boss.csv')

"""
    A classe em questão performa o ETL de acordo com as regras de negócio.
"""


def main():

    commands = Execution()

    log.logging.info("Configuarando componentes")
    commands.create_db()
    commands.set_db()

    log.logging.info(f'Criando as tabelas Bill, Price e Components')
    commands.create_table()

    log.logging.info("Processo de ingestão iniciado")
    commands.insert_data_bill(bill)
    commands.insert_data_price(price)
    commands.insert_data_components(comp)


    return True


if __name__ == '__main__':
    var = main()


