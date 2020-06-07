import pandas as pd
from utils import utils, log


class Components:
    """
        Os métodos abaixam perfomam as transformações necessárias para a ingestão na tabela Components.
    """

    def __init__(self, file):
        self.components = file

    def run(self):
        try:
            df = pd.read_csv(self.components)
            df = df.fillna(0).replace(r'[^0-9a-zA-Z]', '', regex=True)
            df['component_id'] = df['component_id'].replace(r'[^0-9]', '', regex=True)
            df['component_type_id'] = df['component_type_id'].replace(r'[^0-9]', '', regex=True)
            df['connection_type_id'] = df['connection_type_id'].replace(r'[^0-9]', '', regex=True)
            df['height_over_tube'] = df['height_over_tube'].astype(int)
            df['bolt_pattern_long'] = df['bolt_pattern_long'].astype(int)
            df['bolt_pattern_wide'] = df['bolt_pattern_wide'].astype(int)
            df['base_diameter'] = df['base_diameter'].astype(float)
            df['shoulder_diameter'] = df['shoulder_diameter'].astype(float)
            df['weight'] = df['weight'].astype(float)

            utils.data_values('COMPONENTS', df)
            return df

        except pd.errors.ParserError:
            utils.data_error()
        except FileNotFoundError as file:
            utils.not_exists(file)



