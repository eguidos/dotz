import pandas as pd
from utils import utils


def transform_str_columns(df: pd.DataFrame, upper: bool = True, fillna_value: str = "N/A"):
    for col in df.columns:
        if df[col].dtype == "object":
            if upper:
                df[col] = df[col].str.upper()

            df[col].fillna(fillna_value, inplace=True)
            return df


class Pricing:
    def __init__(self, file):
        self._bill = file

    @staticmethod
    def set_cost_by_assembly(group):
        if group["bracket_pricing"].unique() == 1:
            group.sort_values(by="quantity")
            group["previous_quantity"] = group["quantity"].shift(1).fillna(0)
            group = group[
                (group["quantity"] >= group["ammont_to_buy"]) & (group["ammont_to_buy"] > group["previous_quantity"])
                ]

        return group

    def run(self):
        try:
            df = pd.read_csv(self._bill, index_col=False)
            df = transform_str_columns(df, upper=True, fillna_value="N/A")
            df = df.replace(r'[^0-9]', '', regex=True)

            df = df[df["annual_usage"] != 0]
            df["amount_to_buy"] = df[["annual_usage", "min_order_quantity"]].max(axis=1)
            df["annual_cost"] = df["cost"] * df["amount_to_buy"]

            df = df.groupby(['tube_assembly_id']).apply(self.set_cost_by_assembly)

            utils.data_values('price', df)

            return df

        except pd.errors.ParserError:
            utils.data_error()
        except FileNotFoundError as file:
            utils.not_exists(file)
        finally:
            utils.data_values('price', self._bill)


