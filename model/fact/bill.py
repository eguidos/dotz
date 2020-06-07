import pandas as pd
from utils import utils


class Billing:

    def __init__(self, file):
        self._bill = file

    def run(self):
        try:
            df = pd.read_csv(self._bill)
            df = pd.wide_to_long(
                df=df,
                stubnames=["component_id", "quantity"],
                i="tube_assembly_id",
                j="order",
                sep="_"
            ).reset_index(). \
                sort_values(["tube_assembly_id", "order"]). \
                drop("order", axis=1)
            df = df.dropna(subset=["component_id"])
            df = df.groupby(['tube_assembly_id', 'component_id'])["quantity"].sum().reset_index()
            df['tube_assembly_id'] = df['tube_assembly_id'].replace(r'[^0-9]', '', regex=True)
            df['component_id'] = df['component_id'].replace(r'[^0-9]', '', regex=True)

            utils.data_values('Price', df)
            return df

        except pd.errors.ParserError:
            utils.data_error()









