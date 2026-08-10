from datetime import datetime
from faker import Faker
from pathlib import Path
import pandas as pd
import random

fake = Faker()
procedure_lst = []
def gen_procedures(n, pcd_lst):
    for  i in range(n):
        procedure_lst.append(
            {
                "procedure_code": fake.md5(),
                "description": fake.text(max_nb_chars=50),
                "expected_duration_minutes": fake.random_int(min=1, max=3600),
                "expected_cost": fake.random_int(min=50, max=15000),
                "bundled_group": fake.random_element(elements=pcd_lst),
                "is_billable": fake.random_choices(elements=['Yes','No'])
            }
        )
    df = pd.DataFrame(procedure_lst)
    base_path = Path(__file__).resolve().parent.parent
    file_name = '/output/procedure_' + str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) + '.csv'
    file_path = str(base_path) + file_name
    df.to_csv(file_path, index = False)
    return df
    