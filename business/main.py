from DAO.exect import Execution
from commom import utils
from commom import log
bill = utils.get_path('./bill_of_materials.csv')
price = utils.get_path('./price_quote.csv')
comp = utils.get_path('./comp_boss.csv')

"""
    A classe em questão performa o ETL de acordo com as regras de negócio.
"""


def main():

    commands = Execution()
    commands.create_db()
    commands.set_db()
    commands.create_table()
    commands.insert_data_bill(bill)
    commands.insert_data_price(price)
    commands.insert_data_components(comp)

    return True


if __name__ == '__main__':
    var = main()


