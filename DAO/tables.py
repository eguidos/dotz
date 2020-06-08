def create_price():
    price = """CREATE TABLE IF NOT EXISTS price(
                    tube_assembly_id int NOT NULL,
                    supplier varchar(15) NOT NULL,
                    quote_date varchar(30) NOT NULL,
                    annual_usage int NOT NULL,
                    min_order_quantity int NOT NULL,
                    bracket_pricing varchar(3) NOT NULL,
                    quantity int NOT NULL,
                    cost decimal(10,2),
                    amount_to_buy decimal(10,2), 
                    annual_cost decimal(10,2),
                    PRIMARY KEY (tube_assembly_id)
        );"""
    return price


def create_components():
    components = """
        CREATE TABLE IF NOT EXISTS components(
            component_id int NOT NULL,
            component_type_id int NOT NULL,
            type varchar(10) NOT NULL,
            connection_type_id int NOT NULL,
            outside_shape varchar(10) NOT NULL,
            base_type varchar(10) NOT NULL,
            height_over_tube decimal(10,2),
            bolt_pattern_long decimal(10,2),
            bolt_pattern_wide decimal(10,2),
            groove varchar(23) NOT NULL,
            base_diameter decimal(10,2) NOT NULL,
            shoulder_diameter decimal(10,2) NOT NULL,
            unique_feature varchar(3) NOT NULL,
            orientation varchar(3) NOT NULL,
            weight decimal(10,2) NOT NULL,
            PRIMARY KEY(component_id)               
        );"""

    return components

def create_bill():
    bill = """
        CREATE TABLE IF NOT EXISTS bill(
            tube_assembly_id int,
            component_id int,
            quantity int NOT NULL,
            FOREIGN KEY (tube_assembly_id) REFERENCES `price`(`tube_assembly_id`),
            FOREIGN KEY (component_id) REFERENCES `components`(`component_id`)
        );
    """
    return bill
