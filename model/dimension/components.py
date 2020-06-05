import pandas as pd

class Components:
    def __init__(self, file):
        self.components = file

    def run(self):
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
        return df