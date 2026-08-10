from faker import Faker 
from datetime import datetime
from pathlib import Path 
import pandas as pd
import random
import config

fake = Faker()
taxonomy = []
def gen_taxonomy(n, ):
    for i in range(n):
        taxonomy.append(
            {
                "taxonomy_code": f"{i + 1:010}x",
                "specialty": random.choice(config.SPECIALTITY),
                "provider_type": random.choice(["Physician","Hospital"]),
            }
        )
    base_path = Path(__file__).resolve().parent.parent
    file_name = str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    file_path = str(base_path) + '/output/taxonomy_' + file_name + '.csv'
    df = pd.DataFrame(taxonomy)
    df.to_csv(file_path, index=False)
    return df    